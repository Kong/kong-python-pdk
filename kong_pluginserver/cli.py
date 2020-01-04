#!/usr/bin/env python
# coding:utf-8
# Contributor:
#      fffonion        <fffonion@gmail.com>

import os
import re
import argparse
import traceback

from . import PluginServer
from .server import UnixStreamServer
from .logger import Logger

def start():
    parser = argparse.ArgumentParser(description='Kong Python Plugin Server.')
    parser.add_argument('-s', '--socket', metavar='socket', type=str,
                        default="/usr/local/kong/servroot/go_pluginserver.sock",
                        help='Unix domain socket path to listen')
    parser.add_argument('-v', '--verbose', action='count', default = Logger.INFO,
                        help='Turn on verbose logging')
    args = parser.parse_args()

    path = os.path.split(args.socket)[0]
    if not os.path.exists(path):
        raise OSError("path %s doesn't exist, can't create unix socket file" % path)

    ss = UnixStreamServer(PluginServer(loglevel=Logger.WARNING - args.verbose), args.socket)
    ss.serve_forever()
    