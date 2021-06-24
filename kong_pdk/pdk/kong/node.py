# AUTO GENERATED BASED ON Kong 2.4.x, DO NOT EDIT
# Original source path: kong/pdk/node.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str


class node():


    @staticmethod
    def get_hostname() -> str:
        """
        local hostname = kong.node.get_hostname()
        :returns The local machine hostname
        """
        pass

    @staticmethod
    def get_id() -> str:
        """
        local id = kong.node.get_id()
        :returns The v4 UUID used by this node as its id
        """
        pass

    @staticmethod
    def get_memory_stats(unit: Optional[str], scale: Optional[number]) -> table:
        """
        local res = kong.node.get_memory_stats()
        -- res will have the following structure:
        {
        lua_shared_dicts = {
        kong = {
        allocated_slabs = 12288,
        capacity = 24576
        },
        kong_db_cache = {
        allocated_slabs = 12288,
        capacity = 12288
        }
        },
        workers_lua_vms = {
        {
        http_allocated_gc = 1102,
        pid = 18004
        },
        {
        http_allocated_gc = 1102,
        pid = 18005
        }
        }
        }
        local res = kong.node.get_memory_stats("k", 1)
        -- res will have the following structure:
        {
        lua_shared_dicts = {
        kong = {
        allocated_slabs = "12.0 KiB",
        capacity = "24.0 KiB",
        },
        kong_db_cache = {
        allocated_slabs = "12.0 KiB",
        capacity = "12.0 KiB",
        }
        },
        workers_lua_vms = {
        {
        http_allocated_gc = "1.1 KiB",
        pid = 18004
        },
        {
        http_allocated_gc = "1.1 KiB",
        pid = 18005
        }
        }
        }
        :param unit: The unit memory should be reported in. Can be
        either of `b/B`, `k/K`, `m/M`, or `g/G` for bytes, kibibytes, mebibytes,
        or gibibytes, respectively. Defaults to `b` (bytes).
        :param scale: The number of digits to the right of the decimal
        point. Defaults to 2.
        :returns A table containing memory usage statistics for this node.
        If `unit` is `b/B` (the default) reported values will be Lua numbers.
        Otherwise, reported values will be a string with the unit as a suffix.
        """
        pass

    pass