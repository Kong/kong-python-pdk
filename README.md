# kong-python-pluginserver

[![PyPI version](https://badge.fury.io/py/kong-pluginserver.svg)](https://badge.fury.io/py/kong-pluginserver)

Plugin server for Python language support in Kong plugin.

Requires Kong >= 2.0.0.

## Install the plugin server

```shell
pip3 install kong-pluginserver
# Replace the go-pluginserver with python plugin server
cp /usr/local/bin/kong-pluginserver /usr/local/bin/go-pluginserver
```

## Configure Kong

Add the following line into `kong.conf`:

```
plugins=bundled,py-hello,py-image
go_plugins_dir=/your/path/to/python/plugins/dir
```

For example, to test examples, clone `kong-python-pluginserver` to `/dir1/kong-python-pluginserver`
and set `go_plugins_dir` to `/dir1/kong-python-pluginserver/examples`

## Enable the plugin

Same step as it's a Lua plugin.

## Notes

- All PDK API supported by Go Plugin Server is supported.
- The plugin server is implemented by gevent module for now, thus only one CPU core will be used. If your plugin is CPU-hungry, consider run the plugin instance in a seperate process and implement a piping IPC.
- Currently you can't run Go plugins and Python plugins at the same time,
as Kong only accepts one plugin server socket.

## TODO

- Process per instance
- Tests
- Hot reload
