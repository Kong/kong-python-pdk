# coding:utf-8
# Contributor:
#      fffonion        <fffonion@gmail.com>

import os
import sys
import argparse
import msgpack
import json

from .server import PluginServer
from .listener import UnixStreamServer, DEFAULT_SOCKET_NAME
from .logger import Logger

from .const import __version__, PY3K

def parse(dedicated=False):
    parser = argparse.ArgumentParser(description='Kong Python Plugin Server.')
    parser.add_argument('-p', '--kong-prefix', '-kong-prefix',
                        dest='prefix', metavar='prefix', type=str,
                        default="/usr/local/kong/",
                        help='unix domain socket path to listen (default: %(default)s)')
    parser.add_argument('-v', '--verbose', action='count', default=1,
                        help='turn on verbose logging (default: %(default)s)')
    parser.add_argument('--version', '-version', action='version',
                        version='%(prog)s {version}'.format(version=__version__))
    parser.add_argument('--socket-name', type=str, dest='socket_name', default=DEFAULT_SOCKET_NAME,
                        help='socket name to listen on (default: %(default)s)')
    parser.add_argument('--listen-queue-size', type=int, dest='listen_queue_size', default=4096,
                        help='socket listen queue size (default: %(default)s)')
    parser.add_argument('--no-lua-style', action='store_true', dest='no_lua_style', default=False,
                        help='turn off Lua-style "data, err" return values for PDK functions '
                             'and throw exception instead (default: %(default)s)')
    mxg = parser.add_mutually_exclusive_group()
    mxg.add_argument('-m', '--multiprocessing', dest='multiprocessing', action="store_true",
                     help='enable multiprocessing (default: %(default)s)')
    mxg.add_argument('-g', '--gevent', dest='gevent', action="store_true",
                     help='enable gevent (default: %(default)s)')

    if not dedicated:
        parser.add_argument('-d', '--plugins-directory', '-plugins-directory',
                            dest='directory', metavar='directory', type=str, required=True,
                            help='plugins directory')
        parser.add_argument('--dump-plugin-info', '-dump-plugin-info', dest='dump_info', metavar='name', type=str,
                            help='dump specific plugin info into stdout')
        parser.add_argument('--dump-all-plugins', '-dump-all-plugins', dest='dump_all_info', action="store_true",
                            help='dump all plugins info into stdout')
    else:
        parser.add_argument('--dump', '-dump', dest='dump', action="store_true",
                            help='dump current plugin info into stdout')

    args = parser.parse_args()

    if ((not dedicated and not args.dump_info and not args.dump_all_info)
            or (dedicated and not args.dump)) and not os.path.exists(args.prefix):
        raise OSError("path %s doesn't exist, can't create unix socket file" % args.prefix)

    return args

def display_lua_style_notice(lua_style, ps):
    if not lua_style:
        ps.logger.debug("python-style return values are enabled, "
                        "errors are thrown as exception")
    else:
        ps.logger.warn("lua-style return values are used, "
                       "this will be deprecated in the future; instead of returning "
                       "(data, err) tuple, only data will be returned and err will be "
                       "thrown as PDKException; please adjust your plugin to use the "
                       "new python-style PDK API.")

def start_server():
    args = parse()

    prefix = args.prefix

    ps = PluginServer(loglevel=Logger.WARNING - args.verbose,
                      plugin_dir=args.directory,
                      use_multiprocess=args.multiprocessing,
                      use_gevent=args.gevent,
                      lua_style=not args.no_lua_style)
    ss = UnixStreamServer(ps, prefix,
                          sock_name=args.socket_name,
                          use_gevent=args.gevent,
                          listen_queue_size=args.listen_queue_size)
    if args.dump_info:
        ret, err = ps.get_plugin_info(args.dump_info)
        if err:
            raise Exception("error dump info: " + err)
        if PY3K:
            sys.stdout.buffer.write(msgpack.packb(ret))
        else:
            sys.stdout.write(msgpack.packb(ret))
        sys.exit(0)
    elif args.dump_all_info:
        ret = []
        for p in ps.plugins:
            inf = ps.get_plugin_info(p)
            ret.append(inf)
        sys.stdout.write(json.dumps(ret))
        sys.exit(0)

    display_lua_style_notice(not args.no_lua_style, ps)

    try:
        ss.serve_forever()
    except KeyboardInterrupt:
        ps.logger.info("polite exit requested, terminating...")

    ps.cleanup()

def start_dedicated_server(name, plugin, _version=None, _priority=0, _schema=[]):
    from .module import Module

    args = parse(dedicated=True)

    ps = PluginServer(loglevel=Logger.WARNING - args.verbose,
                      use_multiprocess=args.multiprocessing,
                      use_gevent=args.gevent,
                      name="%s version %s" % (name, _version or 'unknown'),
                      lua_style=not args.no_lua_style)
    socket_name = args.socket_name
    if socket_name == DEFAULT_SOCKET_NAME:
        socket_name = "%s.sock" % name
    ss = UnixStreamServer(ps, args.prefix,
                          sock_name=socket_name,
                          use_gevent=args.gevent,
                          listen_queue_size=args.listen_queue_size)

    class mod(object):
        Plugin = plugin
        Schema = _schema
        version = _version
        priority = _priority

    mod = Module(name, module=mod)
    ps.plugins[name] = mod

    if args.dump:
        ret = ps.get_plugin_info(name)
        # note a list is returned
        sys.stdout.write(json.dumps([ret]))
        sys.exit(0)

    display_lua_style_notice(not args.no_lua_style, ps)

    try:
        ss.serve_forever()
    except KeyboardInterrupt:
        ps.logger.info("polite exit requested, terminating...")

    ps.cleanup()
