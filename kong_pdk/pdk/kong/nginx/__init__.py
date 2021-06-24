# AUTO GENERATED BASED ON Kong 2.4.x, DO NOT EDIT
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
        
        :param k: key for the ctx data
        :returns the per-request context data in ngx.ctx
        """
        pass

    @staticmethod
    def get_subsystem() -> str:
        """
        
        :returns the subsystem name
        """
        pass

    @staticmethod
    def get_tls1_version_str() -> str:
        """
        
        :returns the TLSv1 version string
        """
        pass

    @staticmethod
    def get_var() -> str:
        """
        
        :returns the NGINX version string
        """
        pass

    @staticmethod
    def req_start_time() -> number:
        """
        
        :returns req_start_time
        """
        pass

    @staticmethod
    def set_ctx(k: str, any: str) -> None:
        """
        
        :param k: key for the ctx data
        :param any: value for the ctx data
        """
        pass

    pass