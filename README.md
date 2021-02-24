# kong-python-pluginserver

[![PyPI version](https://badge.fury.io/py/kong-pdk.svg)](https://badge.fury.io/py/kong-pdk)

Plugin server and PDK (Plugin Development Kit) for Python language support in Kong.

Requires Kong >= 2.3.0.

## Install the plugin server

```shell
pip3 install kong-pdk
```

## Usage

```
usage: kong-pluginserver.py [-h] [-p prefix] [-v] [--version]
                            [--socket-name SOCKET_NAME] [-m | -g] -d directory
                            [--dump-plugin-info name] [--dump-all-plugins]

Kong Python Plugin Server.

optional arguments:
  -h, --help            show this help message and exit
  -p prefix, --kong-prefix prefix, -kong-prefix prefix
                        unix domain socket path to listen
  -v, --verbose         turn on verbose logging
  --version, -version   show program's version number and exit
  --socket-name SOCKET_NAME
                        socket name to listen on
  -m, --multiprocessing
                        enable multiprocessing
  -g, --gevent          enable gevent
  -d directory, --plugins-directory directory, -plugins-directory directory
                        plugins directory
  --dump-plugin-info name, -dump-plugin-info name
                        dump specific plugin info into stdout
  --dump-all-plugins, -dump-all-plugins
                        dump all plugins info into stdout
```

## Configure Kong

Add the following line into `kong.conf`:

```
plugins=bundled,py-hello,py-image
pluginserver_names=go, py
pluginserver_py_socket=/usr/local/kong/python_pluginserver.sock
pluginserver_py_start_cmd=/usr/local/bin/kong-python-pluginserver -d /dir/to/kong-python-pdk/examples
pluginserver_py_query_cmd=/usr/local/bin/kong-python-pluginserver -d /dir/to/kong-python-pdk/examples --dump-all-plugins
```

For example, to test examples, clone `kong-python-pdk` to `/dir/to/kong-python-pdk`.

To use seperate instance for each plugin, use:

```
plugins=bundled,py-hello,py-image
pluginserver_names=go, py-hello, py-image

pluginserver_py_hello_socket=/usr/local/kong/py_hello.sock
pluginserver_py_hello_start_cmd=/dir/to/kong-python-pdk/examples/py-hello.py
pluginserver_py_hello_query_cmd=/dir/to/kong-python-pdk/examples/py-hello.py -d

pluginserver_py_image_socket=/usr/local/kong/py_image.sock
pluginserver_py_image_start_cmd=/dir/to/kong-python-pdk/examples/py-image.py
pluginserver_py_image_query_cmd=/dir/to/kong-python-pdk/examples/py-image.py -d
```

## Enable the plugin

Same step as it's a Lua plugin.

## Notes

- All PDK API supported by Go Plugin Server is supported.
- If your plugins are CPU intensive, consider using multiprocessing mode (`-m` flag) or run the plugin instance in a seperate process (examples/py-hello.py as an example) to distribute workloads to multicore.
- If your plugins are I/O intensive, considering using gevent mode (`-g` flag) and use gevent libraries in the plugin.


## TODO

- Tests
- Hot reload
