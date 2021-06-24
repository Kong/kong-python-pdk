# AUTO GENERATED BASED ON Kong 2.4.x, DO NOT EDIT
# Original source path: kong/pdk/ctx/shared.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str


class shared():


    @staticmethod
    def get(k: str) -> Any:
        """
        
        :param k: key for the ctx data
        :returns the per-request context data in ngx.ctx
        """
        pass

    @staticmethod
    def set(k: str, v: str) -> None:
        """
        
        :param k: key for the ctx data
        :param v: value for the ctx data
        """
        pass

    pass