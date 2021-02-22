# kong-python-pluginserver

[![PyPI version](https://badge.fury.io/py/kong-pluginserver.svg)](https://badge.fury.io/py/kong-pluginserver)

Plugin server and PDK (Plugin Development Kit) for Python language support in Kong.

Requires Kong >= 2.3.0.

## Install the plugin server

```shell
pip3 install kong-pdk
```

## Configure Kong

Add the following line into `kong.conf`:

```
plugins=bundled,py-hello,py-image
pluginserver_names=go, py
pluginserver_py_socket=/usr/local/kong/python_pluginserver.sock
pluginserver_py_start_cmd=/usr/local/bin/kong-pluginserver -d /dir/to/kong-python-pluginserver/examples
pluginserver_py_query_cmd=/usr/local/bin/kong-pluginserver -d /dir/to/kong-python-pluginserver/examples --dump-all-plugins
```

For example, to test examples, clone `kong-python-pluginserver` to `/dir/to/kong-python-pluginserver`.

## Enable the plugin

Same step as it's a Lua plugin.

## Notes

- All PDK API supported by Go Plugin Server is supported.
- The plugin server is implemented by gevent module for now, thus only one CPU core will be used. If your plugin is CPU-hungry, consider run the plugin instance in a seperate process (examples/py-hello.py as an example).


## TODO

- Close signal handler?
- Tests
- Hot reload
