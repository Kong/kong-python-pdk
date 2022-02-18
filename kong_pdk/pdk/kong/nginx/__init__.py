# AUTO GENERATED BASED ON Kong 2.7.x, DO NOT EDIT
# Original source path: kong/pdk/nginx.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str

from .shared import shared as cls_shared

class nginx():

    shared = cls_shared

    @staticmethod
    def get_ctx(k: str) -> Any:
        """

            get a key-value pair from Kong's per-request context

        :parameter k: key for the ctx data
        :type k: str

        :return: the per-request context data in ngx.ctx

        :rtype: Any
        """
        pass

    @staticmethod
    def get_subsystem() -> str:
        """

        :return: the subsystem name

        :rtype: str
        """
        pass

    @staticmethod
    def get_tls1_version_str() -> str:
        """

        :return: the TLSv1 version string

        :rtype: str
        """
        pass

    @staticmethod
    def get_var() -> str:
        """

        :return: the NGINX version string

        :rtype: str
        """
        pass

    @staticmethod
    def req_start_time() -> number:
        """

            get the current request's start timestamp

        :return: req_start_time

        :rtype: number
        """
        pass

    @staticmethod
    def set_ctx(k: str, any: str) -> None:
        """

            set a key-value pair in Kong's per-request context

        :parameter k: key for the ctx data
        :type k: str
        :parameter any: value for the ctx data
        :type any: str

        """
        pass

    pass