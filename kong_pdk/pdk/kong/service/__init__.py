# AUTO GENERATED BASED ON Kong 2.4.x, DO NOT EDIT
# Original source path: kong/pdk/service.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str

from .request import request as cls_request
from .response import response as cls_response

class service():

    request = cls_request
    response = cls_response

    @staticmethod
    def set_target(host: str, port: number) -> None:
        """
        kong.service.set_target("service.local", 443)
        kong.service.set_target("192.168.130.1", 80)
        :param host: 
        :param port: 
        """
        pass

    @staticmethod
    def set_tls_verify(on: bool) -> Tuple[bool, str]:
        """
        local ok, err = kong.service.set_tls_verify(true)
        if not ok then
        -- do something with error
        end
        :param on: Whether to enable TLS certificate verification for the current request
        :returns `true` if the operation succeeded, `nil` if an error occurred
        returns An error message describing the error if there was one
        """
        pass

    @staticmethod
    def set_tls_verify_depth(depth: number) -> Tuple[bool, str]:
        """
        local ok, err = kong.service.set_tls_verify_depth(3)
        if not ok then
        -- do something with error
        end
        :param depth: Depth to use when validating. Must be non-negative
        :returns `true` if the operation succeeded, `nil` if an error occurred
        returns An error message describing the error if there was one
        """
        pass

    @staticmethod
    def set_upstream(host: str) -> Tuple[bool, str]:
        """
        local ok, err = kong.service.set_upstream("service.prod")
        if not ok then
        kong.log.err(err)
        return
        end
        :param host: 
        :returns `true` on success, or `nil` if no upstream entities
        where found
        returns An error message describing the error if there was
        one.
        """
        pass

    pass