import sys
import os
import time
import json
import gevent
from gevent.lock import Semaphore
from gevent.queue import Channel

from .pdk import Kong
from .module import Module
from .exception import PluginServerException
from .logger import Logger

exts = ('.py', '.pyd', '.so')
entities = ( 'service', 'consumer', 'route', 'plugin', 'credential', 'memory_stats')

def locked_by(lock_name):
    def f(fn):
        def wrapper(*args,**kwargs):
            self = args[0]
            lock = getattr(self, lock_name)
            lock.acquire()
            try:
                r = fn(*args, **kwargs)
            except Exception as ex:
                lock.release()
                raise(ex)
            lock.release()
            return r
        return wrapper

    return f

class PluginServer(object):
    def __init__(self, loglevel=Logger.WARNING, expire_ttl=60):
        self.plugin_dir = None
        self.plugins = {}
        self.p_lock = Semaphore()
        self.instances = {}
        self.instance_id = 0
        self.i_lock = Semaphore()
        self.events = {}
        self.event_id = 0
        self.e_lock = Semaphore()

        self.logger = Logger()
        self.logger.set_level(loglevel)

        # start cleanup timer
        gevent.spawn(self._clear_expired_plugins, expire_ttl)
    
    def _clear_expired_plugins(self, ttl):
        while True:
            gevent.sleep(ttl)
            self.i_lock.acquire()
            keys = list(self.instances.keys())
            for iid in keys:
                instance = self.instances[iid]
                if instance.is_expired(ttl):
                    self.logger.debug("cleanup instance #%d of %s" % (iid, instance.name))
                    del(self.instances[iid])
            self.i_lock.release()

    @locked_by("p_lock")
    def _load_plugin(self, name):
        if not self.plugin_dir:
            raise PluginServerException("plugin server is not initialized, call SetPluginDir first")
        if name in self.plugins:
            return self.plugins[name]
        path = None
        for ext in exts:
            find = os.path.join(self.plugin_dir, name + ext)
            if os.path.exists(find):
                path = find
        if not path:
            raise PluginServerException("plugin not found")

        mod = Module(name, path)
    
        self.plugins[name] = mod
        return mod

    def set_plugin_dir(self, dir):
        if not os.path.exists(dir):
            return None, dir + " not exists"
        self.plugin_dir = dir
        return "ok", None

    @locked_by("p_lock")
    @locked_by("i_lock")
    def get_status(self, *_):
        plugin_status = {}
        for name in self.plugins:
            instances = []
            for iid in self.instances:
                i, err = self.instance_status(iid)
                if err:
                    raise PluginServerException(err)
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
        }, None

    def get_plugin_info(self, name):
        plugin = self._load_plugin(name)

        info = {
            "Name" : name,
            "Phases" : plugin.phases,
            "Priority": plugin.priority,
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
        return info, None
        
    @locked_by("i_lock")
    def start_instance(self, cfg):
        name = cfg['Name']
        config = json.loads(cfg['Config'])
        plugin = self._load_plugin(name)
        iid = self.instance_id
        self.instances[iid] = plugin.new(config)
        self.instance_id = iid + 1
        
        self.logger.info("instance #%d of %s started" % (iid, name))

        return {
            "Name": name,
            "Id": iid,
            "Config": config,
            "StartTime": time.time()
        }, None

    def instance_status(self, iid):
        if iid not in self.instances:
            return None, "instance #%s not found" % iid
        ins = self.instances[iid]
        return {
            "Name": ins.name,
            "Id": iid,
            "Config": ins.config,
            "StartTime": ins.start_time,
        }, None

    @locked_by("i_lock")
    def close_instance(self, iid):
        if iid not in self.instances:
            return None, "instance #%s not found" % iid
        ins = self.instances[iid]
        ins.close_cb()
        del(self.instances[iid])
        return {
            "Name": ins['name'],
            "Id": iid,
            "Config": ins['config'],
        }, None

    @locked_by("e_lock")
    def handle_event(self, event):
        iid = event['InstanceId']
        if iid not in self.instances:
            raise PluginServerException("instance id %s not found" % iid)
        instance = self.instances[iid]
        instance.reset_expire_ts()
        cls = instance.cls
        phase = event['EventName']

        eid = self.event_id
        # plugin communites to Kong (RPC client) in a reverse way
        ch = Channel()
        self.events[eid] = ch
        self.event_id = eid + 1

        gevent.spawn(lambda:(
            getattr(cls, phase)(Kong(ch).kong),
            instance.reset_expire_ts(),
            ch.put("ret")
        ))

        return {
            "Data": ch.get(),
            "EventId": eid,
        }, None
    
    def _step(self, data, is_error):
        eid = data['EventId']
        if eid not in self.events:
            raise PluginServerException("event id %s not found" % eid)
        dd = None
        if 'Data' in data:
            dd = data['Data']
        ch = self.events[eid]
        if is_error:
            ch.put((
                None, dd
            ))
        else:
            ch.put((
                dd, None
            ))

        ret = ch.get()
        if ret == "ret":
            del self.events[eid]
        return {
            "Data": ret,
            "EventId": eid,
        }, None

    def step(self, data):
        return self._step(data, False)

    def step_error(self, data):
        return self._step(data, True)

for entity in entities:
    setattr(PluginServer, 'step_' + entity, PluginServer.step)