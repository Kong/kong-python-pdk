# AUTO GENERATED BASED ON Kong 3.1.x, DO NOT EDIT
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

            Returns the current `route` entity. The request is matched against this
            route.

        Phases:
            access, header_filter, response, body_filter, log

        Example:
            route = kong.router.get_route()

            protocols = route.protocols

        :return: The `route` entity.

        :rtype: table
        """
        pass

    @staticmethod
    def get_service() -> table:
        """

            Returns the current `service` entity. The request is targeted to this
            upstream service.

        Phases:
            access, header_filter, response, body_filter, log

        Example:
            if kong.router.get_service():

                # routed by route & service entities

            else:

                # routed by a route without a service

        :return: The `service` entity.

        :rtype: table
        """
        pass

    pass