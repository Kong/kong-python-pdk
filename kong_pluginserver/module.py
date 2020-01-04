import os
import time
from .const import PY3K
if PY3K:
    import importlib.util
    def load_module(name, path):
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
else:
    import imp
    methods = {
        '.py': imp.load_source,
        '.pyc': imp.load_compiled,
        '.pyo': imp.load_compiled,
        '.pyd': imp.load_dynamic,
        '.so': imp.load_dynamic,
    }
    def load_module(name, path):
        ext = os.path.splitext(path)[1]
        return methods[ext](name, path)

phases = ("certificate", "rewrite", "log", "access", "preread")

class Module(object):
    def __init__(self, name, path):
        mod = load_module(name, path)

        self.mod = mod
        self.name = name
    
        self.cls = getattr(mod, "Plugin")

        self.phases = []
        for phase in phases:
            if hasattr(self.cls, phase):
                self.phases.append(phase)
        
        self.priority = 0
        self.version = None
        
        for attr in ('version', 'priority'):
            au = attr.upper()
            if hasattr(mod, au):
                setattr(self, attr, getattr(mod, au))
        
        if hasattr(mod, "Schema"):
            self.schema = mod.Schema
        else:
            self.schema = []
        self.load_time = time.time()
        self.mtime = os.stat(path).st_mtime

        self.last_start_instance_time = 0
        self.last_close_instance_time = 0
    
    def new(self, config):
        self.last_start_instance_time = time.time()
        return Instance(self.name, config, self.cls, self.set_last_close_instance_time)

    def set_last_close_instance_time(self):
        self.last_close_instance_time = time.time()


class Instance(object):
    def __init__(self, name, config, cls, close_cb):
        self.cls = cls(config)
        self.name = name
        self.config = config
        self.start_time = time.time()
        self.last_used_time = 0
        self.close_cb = close_cb

    def is_expired(self, ttl=60):
        until = time.time() - ttl
        return self.start_time < until and self.last_used_time < until

    def reset_expire_ts(self):
        self.last_used_time = time.time()
        return self.cls