import os
import time
import json
import asyncio
from .const import PY3K
from .pdk import Kong
from .module import Module
from .exception import PluginServerException
from .logger import Logger

exts = ('.py', '.pyd', '.so')
entities = ('service', 'consumer', 'route', 'plugin', 'credential', 'memory_stats')

MSG_RET = 'ret'

async def _handler_event_func(cls_phase, ch, lua_style):
    cls_phase(Kong(ch, lua_style).kong)
    await ch.put(MSG_RET)

class PluginServer:
    def __init__(self, loglevel=Logger.WARNING, expire_ttl=60, plugin_dir=None, name=None, lua_style=True):
        self.plugin_dir = plugin_dir
        self.plugins = {}
        self.instances = {}
        self.instance_id = 0
        self.events = {}
        self.event_id = 0

        self.logger = Logger()
        self.logger.set_level(loglevel)

        if plugin_dir:
            self._load_plugins()

        self.lua_style = lua_style

        self.instance_lock = asyncio.Lock()
        self.event_lock = asyncio.Lock()
        self.event_id_lock = asyncio.Lock()

        self.logger.debug("plugin server is in asyncio mode")

    async def _clear_expired_plugins(self, ttl):
        while True:
            await asyncio.sleep(ttl)
            keys = list(self.instances.keys())
            for iid in keys:
                instance = self.instances[iid]
                if instance.is_expired(ttl):
                    self.logger.debug(f"cleanup instance #{iid} of {instance.name}")
                    del self.instances[iid]

    def _load_plugins(self):
        if not self.plugin_dir:
            raise PluginServerException("plugin server is not initialized, call SetPluginDir first")

        for p in os.listdir(self.plugin_dir):
            n, ext = os.path.splitext(p)
            if ext in exts:
                path = os.path.join(self.plugin_dir, p)
                try:
                    mod = Module(n, path=path)
                except Exception as ex:
                    self.logger.warn(f"error loading plugin \"{n}\": {ex}")
                else:
                    self.logger.debug(f"loaded plugin \"{n}\" from {path}")
                    self.plugins[n] = mod

    def set_plugin_dir(self, dir):
        if not os.path.exists(dir):
            raise PluginServerException(f"{dir} not exists")
        self.plugin_dir = dir
        return "ok"

    async def get_status(self):
        plugin_status = {}
        for name in self.plugins:
            instances = []
            for iid in self.instances:
                if self.instances[iid].name == name:
                    i = await self.instance_status(iid)
                    instances.append(i)
            plugin = self.plugins[name]
            plugin_status[name] = {
                "Name": name,
                "Modtime": plugin.mtime,
                "LoadTime": plugin.load_time,
                "Instances": instances,
                "LastStartInstance": plugin.last_start_instance_time,
                "LastCloseInstance": plugin.last_close_instance_time,
            }
        return {
            "Pid": os.getpid(),
            "Plugins": plugin_status,
        }

    def get_plugin_info(self, name):
        if name not in self.plugins:
            raise PluginServerException(f"{name} not initialized")

        plugin = self.plugins[name]

        info = {
            "Name": name,
            "Phases": plugin.phases,
            "Priority": plugin.priority,
            "Version": plugin.version,
            "Schema": {
                "name": name,
                "fields": [{
                    "config": {
                        "type": "record",
                        "fields": plugin.schema,
                    }
                }],
            },
        }
        return info

    async def start_instance(self, cfg):
        # async with self.instance_lock:
        name = cfg['Name']
        if name not in self.plugins:
            raise PluginServerException(f"{name} not initialized")
        plugin = self.plugins[name]

        config = json.loads(cfg['Config'])
        iid = self.instance_id
        self.instances[iid] = plugin.new(config)
        self.instance_id = iid + 1

        self.logger.info(f"instance #{iid} of {name} started")

        return {
            "Name": name,
            "Id": iid,
            "Config": config,
            "StartTime": time.time()
        }

    async def instance_status(self, iid):
        if iid not in self.instances:
            raise PluginServerException(f"no plugin instance #{iid}")

        ins = self.instances[iid]

        return {
            "Name": ins.name,
            "Id": iid,
            "Config": ins.config,
            "StartTime": ins.start_time,
        }

    async def close_instance(self, iid):
        # async with self.instance_lock:
        if iid not in self.instances:
            raise PluginServerException(f"no plugin instance #{iid}")

        ins = self.instances[iid]
        ins.close_cb()
        del self.instances[iid]

        return {
            "Name": ins.name,
            "Id": iid,
            "Config": ins.config,
        }

    async def handle_event(self, event):
        iid = event['InstanceId']
        if iid not in self.instances:
            raise PluginServerException(f"no plugin instance #{iid}")

        instance = self.instances[iid]
        instance.reset_expire_ts()
        cls = instance.cls
        phase = event['EventName']

        # async with self.event_id_lock:
        eid = self.event_id
        self.event_id = eid + 1

        ch = asyncio.Queue()
        asyncio.create_task(_handler_event_func(getattr(cls, phase), ch, self.lua_style))

        await asyncio.sleep(0)

        r = await ch.get()
        if r != MSG_RET:
            # async with self.event_lock:
            self.events[eid] = ch
    
        instance.reset_expire_ts()

        return {
            "Data": r,
            "EventId": eid,
        }

    async def step(self, data):
        return await self._step(data, False)

    async def step_error(self, data):
        return await self._step(data, True)

    async def _step(self, data, is_error):
        # async with self.event_lock:
        eid = data['EventId']
        if eid not in self.events:
            raise PluginServerException(f"event id {eid} not found")
        dd = data.get('Data')
        queue = self.events[eid]

        if is_error:
            await queue.put((None, dd))
        else:
            await queue.put((dd, None))
        
        await asyncio.sleep(0)

        ret = await queue.get()

        if ret == MSG_RET or (isinstance(ret, dict) and ret.get("Method") in ("kong.response.exit", "kong.response.error")):
            # async with self.event_lock:
            del self.events[eid]

        return {
            "Data": ret,
            "EventId": eid,
        }

# Add these methods to maintain compatibility with the previous implementation
for entity in entities:
    setattr(PluginServer, f'step_{entity}', PluginServer.step)

setattr(PluginServer, 'step_multi_map', PluginServer.step)