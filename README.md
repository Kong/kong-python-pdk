# kong-python-pluginserver

Plugin server for Python language support in Kong plugin.

Requires Kong >= 2.0.0.

## Run the plugin server

```shell
git clone https://github.com/fffonion/kong-python-pluginserver
python3 ./setup.py install
kong-pluginserver -s KONG_PREFIX/go_pluginserver.sock
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
- If your plugin is CPU-hungry, consider run in a seperate thread. In current `gevent` model,
spending too much time in CPU work will block other requests.
- Currently you can't run Go plugins and Python plugins at the same time,
as Kong only accepts one plugin server socket.

## TODO

- Tests
- Hot reload
