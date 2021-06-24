# AUTO GENERATED BASED ON Kong 2.4.x, DO NOT EDIT
# Original source path: kong/pdk/client/tls.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str


class tls():


    @staticmethod
    def disable_session_reuse() -> Tuple[bool, err]:
        """
        local res, err = kong.client.tls.disable_session_reuse()
        if not res then
        -- do something with err
        end
        :returns true if success, nil if failed
        returns nil if success, or error message if failure
        """
        pass

    @staticmethod
    def get_full_client_certificate_chain() -> Tuple[str, err]:
        """
        local cert, err = kong.client.get_full_client_certificate_chain()
        if err then
        -- do something with err
        end
        if not cert then
        -- client did not complete mTLS
        end
        -- do something with cert
        :returns PEM-encoded client certificate if mTLS handshake
        was completed, nil if an error occurred or client did not present
        its certificate
        returns nil if success, or error message if failure
        """
        pass

    @staticmethod
    def request_client_certificate() -> Tuple[bool, err]:
        """
        local res, err = kong.client.tls.request_client_certificate()
        if not res then
        -- do something with err
        end
        :returns true if request was received, nil if request failed
        returns nil if success, or error message if failure
        """
        pass

    @staticmethod
    def set_client_verify() -> None:
        """
        kong.client.tls.set_client_verify("FAILED:unknown CA")
        """
        pass

    pass