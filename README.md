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
usage: kong-pluginserver [-h] [-p prefix] [-v] [--version] [--socket-name SOCKET_NAME] [--listen-queue-size LISTEN_QUEUE_SIZE]
                         [--no-lua-style] [-m | -g] -d directory [--dump-plugin-info name] [--dump-all-plugins]

Kong Python Plugin Server.

optional arguments:
  -h, --help            show this help message and exit
  -p prefix, --kong-prefix prefix, -kong-prefix prefix
                        unix domain socket path to listen (default: /usr/local/kong/)
  -v, --verbose         turn on verbose logging (default: 1)
  --version, -version   show program's version number and exit
  --socket-name SOCKET_NAME
                        socket name to listen on (default: python_pluginserver.sock)
  --listen-queue-size LISTEN_QUEUE_SIZE
                        socket listen queue size (default: 4096)
  --no-lua-style        turn off Lua-style "data, err" return values for PDK functions and throw exception instead (default: False)
  -m, --multiprocessing
                        enable multiprocessing (default: False)
  -g, --gevent          enable gevent (default: False)
  -d directory, --plugins-directory directory, -plugins-directory directory
                        plugins directory
  --dump-plugin-info name, -dump-plugin-info name
                        dump specific plugin info into stdout
  --dump-all-plugins, -dump-all-plugins
                        dump all plugins info into stdout
```

## Deprecation Notice

In next major release of Kong Python PDK, return values will default to use Python style error handling instead of
Lua style. The new style API can be turned on now with `--no-lua-style`.

```python
# old lua-style PDK API
host, err = kong.request.get_header("host")
if err:
    pass # error handling

# new python-style PDK API
try:
    host = kong.request.get_header("host")
    # no err in return, instead they are thrown if any
except Exception as ex:
    pass # error handling
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
