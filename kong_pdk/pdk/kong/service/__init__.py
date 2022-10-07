# AUTO GENERATED BASED ON Kong 3.1.x, DO NOT EDIT
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

            Sets the host and port on which to connect to for proxying the request.
            Using this method is equivalent to ask Kong to not run the load-balancing
            phase for this request, and consider it manually overridden.
            Load-balancing components such as retries and health-checks will also be
            ignored for this request.
            The `host` argument expects the hostname or IP address of the upstream 
            server, and the `port` expects a port number.

        Phases:
            access

        Example:
            kong.service.set_target("service.local", 443)

            kong.service.set_target("192.168.130.1", 80)

        :parameter host: 
        :type host: str
        :parameter port: 
        :type port: number

        """
        pass

    @staticmethod
    def set_tls_verify(on: bool) -> Tuple[bool, str]:
        """

            Sets whether TLS verification is enabled while handshaking with the Service.
            The `on` argument is a boolean flag, where `true` means upstream verification
            is enabled and `false` disables it.
            This call affects only the current request. If the trusted certificate store is
            not set already (via [proxy_ssl_trusted_certificate](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_ssl_trusted_certificate)
            or [kong.service.set_upstream_ssl_trusted_store](#kongserviceset_upstream_ssl_trusted_store)),
            then TLS verification will always fail with "unable to get local issuer certificate" error.

        Phases:
            rewrite`, access`, balancer`

        Example:
            ok, err = kong.service.set_tls_verify(true)

            if not ok:

                # do something with error

        :parameter on: Whether to enable TLS certificate verification for the current request
        :type on: bool

        :return: `true` if the operation succeeded, `nil` if an error occurred

        :rtype: bool
        :return: An error message describing the error if there was one

        :rtype: str
        """
        pass

    @staticmethod
    def set_tls_verify_depth(depth: number) -> Tuple[bool, str]:
        """

            Sets the maximum depth of verification when validating upstream server's TLS certificate.
            This call affects only the current request. For the depth to be actually used the verification
            has to be enabled with either the [proxy_ssl_verify](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_ssl_verify)
            directive or using the [kong.service.set_tls_verify](#kongserviceset_tls_verify) function.

        Phases:
            rewrite`, access`, balancer`

        Example:
            ok, err = kong.service.set_tls_verify_depth(3)

            if not ok:

                # do something with error

        :parameter depth: Depth to use when validating. Must be non-negative
        :type depth: number

        :return: `true` if the operation succeeded, `nil` if an error occurred

        :rtype: bool
        :return: An error message describing the error if there was one

        :rtype: str
        """
        pass

    @staticmethod
    def set_upstream(host: str) -> Tuple[bool, str]:
        """

            Sets the desired Upstream entity to handle the load-balancing step for
            this request. Using this method is equivalent to creating a Service with a
            `host` property equal to that of an Upstream entity (in which case, the
            request would be proxied to one of the Targets associated with that
            Upstream).
            The `host` argument should receive a string equal to the name of one of the
            Upstream entities currently configured.

        Phases:
            access

        Example:
            ok, err = kong.service.set_upstream("service.prod")

            if not ok:

                kong.log.err(err)

            return

        :parameter host: 
        :type host: str

        :return: `true` on success, or `nil` if no upstream entities
            where found

        :rtype: bool
        :return: An error message describing the error if there was
            one.

        :rtype: str
        """
        pass

    pass