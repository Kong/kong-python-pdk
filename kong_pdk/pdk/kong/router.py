# AUTO GENERATED BASED ON Kong 2.4.x, DO NOT EDIT
# Original source path: kong/pdk/router.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str


class router():


    @staticmethod
    def get_route() -> table:
        """
        local route = kong.router.get_route()
        local protocols = route.protocols
        :returns the `route` entity.
        """
        pass

    @staticmethod
    def get_service() -> table:
        """
        if kong.router.get_service() then
        -- routed by route & service entities
        else
        -- routed by a route without a service
        end
        :returns the `service` entity.
        """
        pass

    pass