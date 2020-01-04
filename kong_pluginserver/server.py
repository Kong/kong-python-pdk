#!/bin/bash
import os
import re
import traceback

from gevent import socket
from gevent.server import StreamServer as gStreamServer
import msgpack

cmdre = re.compile("([a-z])([A-Z])")

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
                ret_c = ret and len(ret)
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

class UnixStreamServer(Server):
    def __init__(self, pluginserver, path):
        Server.__init__(self, pluginserver)
        self.path = path
    
    def serve_forever(self):
        listener = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        if os.path.exists(self.path):
            os.remove(self.path)
        listener.bind(self.path)
        listener.listen(1)

        self.logger.info("server started")

        gStreamServer(listener, self.handle).serve_forever()