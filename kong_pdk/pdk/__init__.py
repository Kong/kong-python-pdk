class FakeClasses(object):
    def __init__(self, prefix, call):
        self.prefix = prefix
        self.call = call
    
    def __call__(self, *a):
        return self.call(self.prefix, *a)
    
    # TODO
    def __str__(self):
        return self.call(self.prefix)
    
    def __getattr__(self, k):
        return FakeClasses(self.prefix + "." + k, self.call)

def rpc_of(ch):
    def f(m, *a):
        ch.put({
            "Method": m,
            "Args": a,
        })
        return ch.get()
    return f

class Kong(object):
    def __init__(self, ch):
        self.kong = FakeClasses("kong", self.bridge)
        self.rpc = rpc_of(ch)

    def bridge(self, attr, *args):
        return self.rpc(attr, *args)
