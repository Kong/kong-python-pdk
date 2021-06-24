# AUTO GENERATED BASED ON Kong 2.4.x, DO NOT EDIT
# Original source path: kong/pdk/cluster.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str


class cluster():


    @staticmethod
    def get_id() -> Tuple[str, str]:
        """
        local id, err = kong.cluster.get_id()
        if err then
        -- handle error
        end
        if not id then
        -- no cluster ID is available
        end
        -- use id here
        :returns The v4 UUID used by this cluster as its id
        returns an error message
        """
        pass

    pass