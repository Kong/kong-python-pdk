# AUTO GENERATED BASED ON Kong 3.1.x, DO NOT EDIT
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

            Depending on the `trusted_ips` configuration property,
            this function returns whether a given IP is trusted or not.
            Both ipv4 and ipv6 are supported.

        Phases:
            init_worker, certificate, rewrite, access, header_filter, response, body_filter, log

        Example:
            if kong.ip.is_trusted("1.1.1.1"):

                kong.log("The IP is trusted")

        :parameter address: A string representing an IP address.
        :type address: str

        :return: `true` if the IP is trusted, `false` otherwise.

        :rtype: bool
        """
        pass

    pass