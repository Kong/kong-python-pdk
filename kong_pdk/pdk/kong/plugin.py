# AUTO GENERATED BASED ON Kong 3.4.x, DO NOT EDIT
# Original source path: kong/pdk/plugin.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str


class plugin():


    @staticmethod
    def get_id() -> str:
        """

            Returns the instance ID of the plugin.

        Phases:
            rewrite, access, header_filter, response, body_filter, log

        Example:
            kong.request.get_id() # "123e4567-e89b-12d3-a456-426614174000"

        :return: The ID of the running plugin

        :rtype: str
        """
        pass

    pass