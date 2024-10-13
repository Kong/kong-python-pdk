import os
import re
import sys
import time
import traceback
import multiprocessing
import msgpack
from multiprocessing import Process, Queue

from .const import PY3K
if PY3K:
    from socketserver import UnixStreamServer as sUnixStreamServer
else:
    from SocketServer import UnixStreamServer as sUnixStreamServer

import gevent
from gevent import socket as gsocket, sleep as gsleep
from gevent.server import StreamServer as gStreamServer

from .exception import PDKException, PluginServerException

cmdre = re.compile("([a-z])([A-Z])")

DEFAULT_SOCKET_NAME = "python_pluginserver.sock"
DEFAULT_NUM_WORKERS = 4

def write_response(fd, msgid, response):
    fd.send(msgpack.packb([
        1,  # is response
        msgid,
        None,
        response
    ]))

def write_error(fd, msgid, error):
    fd.send(msgpack.packb([
        1,  # is response
        msgid,
        error,
        None
    ]))

class WrapSocket(object):
    def __init__(self, socket):
        self.socket = socket

    def read(self, n):
        return self.socket.recv(n)

class Server(object):
    def __init__(self, plugin_server):
        self.ps = plugin_server
        self.logger = plugin_server.logger

    def handle(self, fd, address, *_):
        sockf = WrapSocket(fd)
        unpacker = msgpack.Unpacker(sockf, strict_map_key=False)

        for _, msgid, method, args in unpacker:
            ns, cmd = method.split(".")
            if ns != "plugin":
                write_error(fd, msgid, "RPC for %s is not supported" % ns)
                continue

            cmd_r = cmd[0].lower() + cmdre.sub(lambda m: "%s_%s" % (m.group(1), m.group(2).lower()), cmd[1:])
            try:
                self.logger.debug("rpc: #%d method: %s args: %s" % (msgid, method, args))
                ret = getattr(self.ps, cmd_r)(*args)
                self.logger.debug("rpc: #%d return: %s" % (msgid, ret))
                write_response(fd, msgid, ret)
            except (PluginServerException, PDKException) as ex:
                self.logger.warn("rpc: #%d error: %s" % (msgid, str(ex)))
                write_error(fd, msgid, str(ex))
            except Exception as ex:
                self.logger.error("rpc: #%d exception: %s" % (msgid, traceback.format_exc()))
                write_error(fd, msgid, str(ex))

def gevent_worker(server, sock):
    while True:
        client, _ = sock.accept()
        gevent.spawn(server.handle, client, None)

def standard_worker(server, sock):
    while True:
        client, _ = sock.accept()
        server.handle(client, None)

def watchdog(sleep, logger):
    while True:
        if os.getppid() == 1:  # parent dead, process adopted by init
            logger.info("Kong exits, terminating...")
            sys.exit()
        sleep(1)

class UnixStreamServer(Server):
    def __init__(self, pluginserver, path,
                 sock_name=DEFAULT_SOCKET_NAME, use_gevent=True, listen_queue_size=4096, num_workers=DEFAULT_NUM_WORKERS):
        Server.__init__(self, pluginserver)
        self.path = os.path.join(path, sock_name)
        self.use_gevent = use_gevent
        self.listen_queue_size = listen_queue_size
        self.num_workers = 8

    def serve_forever(self):
        if os.path.exists(self.path):
            os.remove(self.path)

        if self.use_gevent:
            listener = gsocket.socket(gsocket.AF_UNIX, gsocket.SOCK_STREAM)
            listener.bind(self.path)
            listener.listen(self.listen_queue_size)

            self.logger.info(f"server (gevent) started at path {self.path} with {self.num_workers} workers")

            gevent.spawn(watchdog, gsleep, self.logger)

            workers = []
            for _ in range(self.num_workers):
                worker = Process(target=gevent_worker, args=(self, listener))
                worker.daemon = True
                worker.start()
                workers.append(worker)

            for worker in workers:
                worker.join()
        else:
            import socket
            self.logger.info(f"server started at path {self.path} with {self.num_workers} workers")

            watchdog_process = Process(
                target=watchdog,
                args=(time.sleep, self.logger,),
            )
            watchdog_process.daemon = True
            watchdog_process.start()

            s = sUnixStreamServer(self.path, self.handle, bind_and_activate=False)
            s.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
            s.server_bind()
            s.socket.listen(self.listen_queue_size)

            workers = []
            for _ in range(self.num_workers):
                worker = Process(target=standard_worker, args=(self, s.socket))
                worker.daemon = True
                worker.start()
                workers.append(worker)

            for worker in workers:
                worker.join()