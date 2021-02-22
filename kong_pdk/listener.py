import os
import re
import sys
import traceback

from gevent import socket, sleep as gsleep, spawn as gspawn
from gevent.server import StreamServer as gStreamServer
import msgpack

cmdre = re.compile("([a-z])([A-Z])")

DEFAULT_SOCKET_NAME = "python_pluginserver.sock"

def write_response(fd, msgid, response):
    fd.send(msgpack.packb([
        1, # is response
        msgid,
        None,
        response
    ]))

def write_error(fd, msgid, error):
    fd.send(msgpack.packb([
        1, # is response
        msgid,
        error,
        None
    ]))

class Server(object):
    def __init__(self, plugin_server):
        self.ps = plugin_server
        self.logger = plugin_server.logger

    def handle(self, fd, address):
        while True:
            msg = fd.recv(1024)
            if not msg:
                return
            # raw=False: decode to str not bytes
            d = msgpack.unpackb(msg, raw=False)
            _, msgid, method, args = d
            ns, cmd = method.split(".")
            if ns != "plugin":
                write_error(fd, msgid, "RPC for %s is not supported" % ns)
                continue

            cmd_r = cmd[0].lower() + cmdre.sub(lambda m: "%s_%s" % (m.group(1), m.group(2).lower()), cmd[1:])
            try:
                self.logger.debug("rpc: #%d method: %s args: %s" % (msgid, method, args))
                ret = getattr(self.ps, cmd_r)(*args)
                ret_c = ret and len(ret) or 0
                if ret_c != 2:
                    write_error(fd, msgid,
                        "%s should return two arguments, only got %s" % (cmd_r, ret_c))
                    continue
                r, err = ret
                if err:
                    write_error(fd, msgid, err)
                else:
                    write_response(fd, msgid, r)
                continue
            except Exception as ex:
                self.logger.error(traceback.format_exc())
                write_error(fd, msgid, str(ex))
                continue

def watchdog(logger):
    while True:
        if os.getppid() == 1: # parent dead, process adopted by init
            logger.info("Kong exits, terminating...")
            sys.exit()
        gsleep(1)

class UnixStreamServer(Server):
    def __init__(self, pluginserver, path, sock_name=DEFAULT_SOCKET_NAME):
        Server.__init__(self, pluginserver)
        self.path = os.path.join(path, sock_name)
    
    def serve_forever(self):
        listener = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        if os.path.exists(self.path):
            os.remove(self.path)
        listener.bind(self.path)
        listener.listen(1)

        self.logger.info("server started at path " + self.path)

        gspawn(watchdog, self.logger)

        try:
            gStreamServer(listener, self.handle).serve_forever()
        except KeyboardInterrupt:
            self.logger.info("polite exit requested, terminating...")