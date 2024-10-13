import asyncio
#import nest_asyncio
from ..exception import PDKException

class FakeClasses(object):
    def __init__(self, prefix, call):
        self.prefix = prefix
        self.call = call

    def __call__(self, *a):
        # loop = asyncio.get_event_loop()
        # nest_asyncio.apply(loop)
        # r = loop.run_until_complete(self.call(self.prefix, *a))
        # return r
        return self.call(self.prefix, *a)

    # TODO
    def __str__(self):
        # loop = asyncio.get_event_loop()
        # nest_asyncio.apply(loop)
        # return loop.run_until_complete(self.call(self.prefix))
        return self.call(self.prefix)

    def __getattr__(self, k):
        return FakeClasses(self.prefix + "." + k, self.call)


# those methods never return, instead, they exit from current request immediately
non_return_methods = set((
    "kong.response.exit",
    "kong.response.error",
))

def rpc_of(ch, lua_style):
    async def f(m, *a):
        # sanitize non-serializable objects
        if m == "kong.log" or m.startswith("kong.log."):
            a = list(a)
            for i in range(len(a)):
                if type(a[i]) not in (str, int, list, dict):
                    a[i] = str(a[i])

        await ch.put({
            "Method": m,
            "Args": a,
        })

        if m in non_return_methods:
            return
    
        await asyncio.sleep(0)

        data, err = await ch.get()

        if lua_style:
            return data, err
        if err:
            raise PDKException("exception from %s: %s" % (m, err))
        return data
    return f

class Kong(object):
    def __init__(self, ch, lua_style=False):
        self.kong = FakeClasses("kong", self.bridge)
        self.rpc = rpc_of(ch, lua_style)

    def bridge(self, attr, *args):
        return self.rpc(attr, *args)
