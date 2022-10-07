# AUTO GENERATED BASED ON Kong 3.1.x, DO NOT EDIT
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
    def get_statistics() -> table:
        """

            Returns various connection and request metrics exposed by
            Nginx, similar to those reported by the
            [ngx_http_stub_status_module](https://nginx.org/en/docs/http/ngx_http_stub_status_module.html#data).
            The following fields are included in the returned table:
            * `connections_active` - the current number of active client connections including `connections_waiting`.
            * `connections_reading` - the current number of connections where nginx is reading the request header.
            * `connections_writing` - the current number of connections where nginx is writing the response back to the client.
            * `connections_waiting` - the current number of idle client connections waiting for a request.
            * `connections_accepted` - the total number of accepted client connections.
            * `connections_handled` - the total number of handled connections. Same as `connections_accepted` unless some resource limits have been reached
              (for example, the [`worker_connections`](https://nginx.org/en/docs/ngx_core_module.html#worker_connections) limit).
            * `total_requests` - the total number of client requests.

        Example:
            nginx_statistics = kong.nginx.get_statistics()

        :return: Nginx connections and requests statistics

        :rtype: table
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