# AUTO GENERATED BASED ON Kong 3.1.x, DO NOT EDIT
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

            Returns the name used by the local machine.

        Example:
            hostname = kong.node.get_hostname()

        :return: The local machine hostname.

        :rtype: str
        """
        pass

    @staticmethod
    def get_id() -> str:
        """

            Returns the ID used by this node to describe itself.

        Example:
            id = kong.node.get_id()

        :return: The v4 UUID used by this node as its ID.

        :rtype: str
        """
        pass

    @staticmethod
    def get_memory_stats(unit: Optional[str], scale: Optional[number]) -> table:
        """

            Returns memory usage statistics about this node.

        Example:
            res = kong.node.get_memory_stats()

            # res will have the following structure:

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

            res = kong.node.get_memory_stats("k", 1)

            # res will have the following structure:

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

        :parameter unit: The unit that memory is reported in. Can be
            any of `b/B`, `k/K`, `m/M`, or `g/G` for bytes, kibibytes, mebibytes,
            or gibibytes, respectively. Defaults to `b` (bytes).
        :type unit: str
        :parameter scale: The number of digits to the right of the decimal
            point. Defaults to 2.
        :type scale: number

        :return: A table containing memory usage statistics for this node.
            If `unit` is `b/B` (the default), reported values are Lua numbers.
            Otherwise, reported values are strings with the unit as a suffix.

        :rtype: table
        """
        pass

    pass