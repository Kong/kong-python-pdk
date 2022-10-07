# AUTO GENERATED BASED ON Kong 3.1.x, DO NOT EDIT
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

            get a key-value pair from Kong's shared memory

        :parameter k: key for the ctx data
        :type k: str

        :return: the per-request context data in ngx.ctx

        :rtype: Any
        """
        pass

    @staticmethod
    def set(k: str, v: str) -> None:
        """

            set a key-value pair in Kong's shared memory

        :parameter k: key for the ctx data
        :type k: str
        :parameter v: value for the ctx data
        :type v: str

        """
        pass

    pass