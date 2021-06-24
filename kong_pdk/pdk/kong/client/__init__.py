# AUTO GENERATED BASED ON Kong 2.4.x, DO NOT EDIT
# Original source path: kong/pdk/client.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str

from .tls import tls as cls_tls

class client():

    tls = cls_tls

    @staticmethod
    def authenticate(consumer: table, credential: table) -> None:
        """
        -- assuming `credential` and `consumer` have been set by some authentication code
        kong.client.authenticate(consumer, credentials)
        :param consumer: The consumer to set. Note: if no
        value is provided, then any existing value will be cleared!
        :param credential: The credential to set. Note: if
        no value is provided, then any existing value will be cleared!
        """
        pass

    @staticmethod
    def get_consumer() -> table:
        """
        local consumer = kong.client.get_consumer()
        if consumer then
        consumer_id = consumer.id
        else
        -- request not authenticated yet, or a credential
        -- without a consumer (external auth)
        end
        :returns the authenticated consumer entity
        """
        pass

    @staticmethod
    def get_credential() -> str:
        """
        local credential = kong.client.get_credential()
        if credential then
        consumer_id = credential.consumer_id
        else
        -- request not authenticated yet
        end
        :returns the authenticated credential
        """
        pass

    @staticmethod
    def get_forwarded_ip() -> str:
        """
        -- Given a client with IP 127.0.0.1 making connection through
        -- a load balancer with IP 10.0.0.1 to Kong answering the request for
        -- https://username:password@example.com:1234/v1/movies
        kong.client.get_forwarded_ip() -- "127.0.0.1"
        -- Note: assuming that 10.0.0.1 is one of the trusted IPs, and that
        -- the load balancer adds the right headers matching with the configuration
        -- of `real_ip_header`, e.g. `proxy_protocol`.
        :returns ip The remote address of the client making the request,
        considering forwarded addresses
        """
        pass

    @staticmethod
    def get_forwarded_port() -> number:
        """
        -- [client]:40000 <-> 80:[balancer]:30000 <-> 80:[kong]:20000 <-> 80:[service]
        kong.client.get_forwarded_port() -- 40000
        -- Note: assuming that [balancer] is one of the trusted IPs, and that
        -- the load balancer adds the right headers matching with the configuration
        -- of `real_ip_header`, e.g. `proxy_protocol`.
        :returns The remote client port, considering forwarded ports
        """
        pass

    @staticmethod
    def get_ip() -> str:
        """
        -- Given a client with IP 127.0.0.1 making connection through
        -- a load balancer with IP 10.0.0.1 to Kong answering the request for
        -- https://example.com:1234/v1/movies
        kong.client.get_ip() -- "10.0.0.1"
        :returns ip The remote address of the client making the request
        """
        pass

    @staticmethod
    def get_port() -> number:
        """
        -- [client]:40000 <-> 80:[balancer]:30000 <-> 80:[kong]:20000 <-> 80:[service]
        kong.client.get_port() -- 30000
        :returns The remote client port
        """
        pass

    @staticmethod
    def get_protocol(allow_terminated: Optional[bool]) -> Tuple[str, err]:
        """
        kong.client.get_protocol() -- "http"
        :param allow_terminated: . If set, the `X-Forwarded-Proto` header will be checked when checking for https
        :returns `"http"`, `"https"`, `"tcp"`, `"tls"` or `nil`
        returns nil if success, or error message if failure
        """
        pass

    @staticmethod
    def load_consumer(consumer_id: str, search_by_username: Optional[bool]) -> Tuple[table, err]:
        """
        local consumer_id = "john_doe"
        local consumer = kong.client.load_consumer(consumer_id, true)
        :param consumer_id: The consumer id to look up.
        :param search_by_username: . If truthy,
        then if the consumer was not found by id,
        then a second search by username will be performed
        :returns consumer entity or nil
        returns nil if success, or error message if failure
        """
        pass

    pass