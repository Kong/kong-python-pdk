# kong-python-pluginserver

[![PyPI version](https://badge.fury.io/py/kong-pdk.svg)](https://badge.fury.io/py/kong-pdk)

Plugin server and PDK (Plugin Development Kit) for Python language support in Kong.

Requires Kong >= 2.3.0.

## Documentation

- [PDK API Reference](https://kong.github.io/kong-python-pdk/)
- [Examples](https://github.com/Kong/kong-python-pdk/tree/master/examples)

## Installation

Install the plugin server globally with pip:

```
pip3 install kong-pdk
```

## Plugin Development

A valid Python plugin must define:

```python
Schema = (
    { "message": { "type": "string" } },
)
version = '0.1.0'
priority = 0

class Plugin(object):
    pass
```

Each plugin includes:
- A `Plugin` class with optional phase handler methods
- A `Schema` for plugin configuration
- `version` and `priority` values

Example with an `access` handler:

```python
class Plugin(object):
    def __init__(self, config):
        self.config = config

    def access(self, kong):
        host, err = kong.request.get_header("host")
        kong.log.info(f"Host header: {host}")
```

### Supported phases

- `certificate`
- `rewrite`
- `access`
- `response`
- `preread`
- `log`

### Type Hints

For autocomplete in IDEs, you can add type hints:

```python
import kong_pdk.pdk.kong as kong

class Plugin(object):
    def __init__(self, config):
        self.config = config

    def access(self, kong: kong.kong):
        host, err = kong.request.get_header("host")
```

> ⚠️ The `kong` module is only for type hints—always use the `kong` instance passed into the phase handler.

## Embedded Plugin Server

To run the plugin with an embedded server:

```python
if __name__ == "__main__":
    from kong_pdk.cli import start_dedicated_server
    start_dedicated_server("py-hello", Plugin, version, priority)
```

## Kong Configuration

To load a Python plugin in Kong Gateway via `kong.conf`, add:

```
pluginserver_names = my-plugin

pluginserver_my_plugin_start_cmd = /path/to/my-plugin.py
pluginserver_my_plugin_query_cmd = /path/to/my-plugin.py --dump
pluginserver_my_plugin_socket = /usr/local/kong/my-plugin.socket
```

Enable verbose logging:

```
pluginserver_my_plugin_start_cmd = /path/to/my-plugin.py -v
```

## Concurrency Options

You can configure concurrency models in `kong.conf` using:

- `-g` — enables [Gevent](http://www.gevent.org/) for IO-bound workloads
- `-m` — enables multiprocessing for CPU-bound workloads

```
pluginserver_my_plugin_start_cmd = /path/to/my-plugin.py -g
```

## CLI Usage

```
usage: kong-python-pluginserver [-h] [-p prefix] [-v] [--version] [--socket-name SOCKET_NAME] [--listen-queue-size LISTEN_QUEUE_SIZE]
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

## API Reference

The PDK API documentation is available here:  
📚 [https://kong.github.io/kong-python-pdk/](https://kong.github.io/kong-python-pdk/)

To regenerate it locally:

```
git worktree add docs/build/html gh-pages
cd docs
make deps && make html
```
## Using in Containers or Kubernetes

To run Python plugins inside a containerized Gateway, you must ensure the plugin server and plugin code are installed within the Kong container.

Note: Official Kong images run as the `nobody` user. When building a custom image, temporarily switch to `root` to copy dependencies.

Example `Dockerfile`:

```dockerfile
FROM kong
USER root

# Install Python dependencies and the PDK
RUN apk update && \
    apk add python3 py3-pip python3-dev musl-dev libffi-dev gcc g++ file make && \
    PYTHONWARNINGS=ignore pip3 install kong-pdk

# Copy your plugin code into the image
COPY your-py-plugin /path/to/your/py-plugins/your-py-plugin

USER kong
ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOSE 8000 8443 8001 8444
STOPSIGNAL SIGQUIT
HEALTHCHECK --interval=10s --timeout=10s --retries=10 CMD kong health
CMD ["kong", "docker-start"]
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

## TODO

- Tests
- Hot reload
