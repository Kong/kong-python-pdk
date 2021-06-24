# AUTO GENERATED BASED ON Kong 2.4.x, DO NOT EDIT
# Original source path: kong/pdk/ip.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str


class ip():


    @staticmethod
    def is_trusted(address: str) -> bool:
        """
        if kong.ip.is_trusted("1.1.1.1") then
        kong.log("The IP is trusted")
        end
        :param address: A string representing an IP address
        :returns `true` if the IP is trusted, `false` otherwise
        """
        pass

    pass