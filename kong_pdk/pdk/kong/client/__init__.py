# AUTO GENERATED BASED ON Kong 3.1.x, DO NOT EDIT
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

            Sets the authenticated consumer and/or credential for the current request.
            While both `consumer` and `credential` can be `nil`,
            at least one of them must exist. Otherwise, this function will throw an
            error.

        Phases:
            access

        Example:
            # assuming `credential` and `consumer` have been set by some authentication code

            kong.client.authenticate(consumer, credentials)

        :parameter consumer: The consumer to set. If no
            value is provided, then any existing value will be cleared.
        :type consumer: table
        :parameter credential: The credential to set. If
            no value is provided, then any existing value will be cleared.
        :type credential: table

        """
        pass

    @staticmethod
    def get_consumer() -> table:
        """

            Returns the `consumer` entity of the currently authenticated consumer.
            If not set yet, it returns `nil`.

        Phases:
            access, header_filter, response, body_filter, log

        Example:
            consumer = kong.client.get_consumer()

            if consumer:

                consumer_id = consumer.id

            else:

                # request not authenticated yet, or a credential

            # without a consumer (external auth)

        :return: The authenticated consumer entity.

        :rtype: table
        """
        pass

    @staticmethod
    def get_credential() -> str:
        """

            Returns the credentials of the currently authenticated consumer.
            If not set yet, it returns `nil`.

        Phases:
            access, header_filter, response, body_filter, log

        Example:
            credential = kong.client.get_credential()

            if credential:

                consumer_id = credential.consumer_id

            else:

                # request not authenticated yet

        :return: The authenticated credential.

        :rtype: str
        """
        pass

    @staticmethod
    def get_forwarded_ip() -> str:
        """

            Returns the remote address of the client making the request. Unlike
            `kong.client.get_ip`, this function will consider forwarded addresses in
            cases when a load balancer is in front of Kong. Whether this function
            returns a forwarded address or not depends on several Kong configuration
            parameters:
            * [trusted\_ips](https://docs.konghq.com/gateway/latest/reference/configuration/#trusted_ips)
            * [real\_ip\_header](https://docs.konghq.com/gateway/latest/reference/configuration/#real_ip_header)
            * [real\_ip\_recursive](https://docs.konghq.com/gateway/latest/reference/configuration/#real_ip_recursive)

        Phases:
            certificate, rewrite, access, header_filter, response, body_filter, log

        Example:
            # Given a client with IP 127.0.0.1 making connection through

            # a load balancer with IP 10.0.0.1 to Kong answering the request for

            # https://username:password@example.com:1234/v1/movies

            kong.client.get_forwarded_ip() # "127.0.0.1"

            # Note: This example assumes that 10.0.0.1 is one of the trusted IPs, and that

            # the load balancer adds the right headers matching with the configuration

            # of `real_ip_header`, e.g. `proxy_protocol`.

        :return: The remote IP address of the client making the request,
            considering forwarded addresses.

        :rtype: str
        """
        pass

    @staticmethod
    def get_forwarded_port() -> number:
        """

            Returns the remote port of the client making the request. Unlike
            `kong.client.get_port`, this function will consider forwarded ports in cases
            when a load balancer is in front of Kong. Whether this function returns a
            forwarded port or not depends on several Kong configuration parameters:
            * [trusted\_ips](https://docs.konghq.com/gateway/latest/reference/configuration/#trusted_ips)
            * [real\_ip\_header](https://docs.konghq.com/gateway/latest/reference/configuration/#real_ip_header)
            * [real\_ip\_recursive](https://docs.konghq.com/gateway/latest/reference/configuration/#real_ip_recursive)

        Phases:
            certificate, rewrite, access, header_filter, response, body_filter, log

        Example:
            # [client]:40000 <-> 80:[balancer]:30000 <-> 80:[kong]:20000 <-> 80:[service]

            kong.client.get_forwarded_port() # 40000

            # Note: This example assumes that [balancer] is one of the trusted IPs, and that

            # the load balancer adds the right headers matching with the configuration

            # of `real_ip_header`, e.g. `proxy_protocol`.

        :return: The remote client port, considering forwarded ports.

        :rtype: number
        """
        pass

    @staticmethod
    def get_ip() -> str:
        """

            Returns the remote address of the client making the request. This module
            **always** returns the address of the client directly connecting to Kong.
            That is, in cases when a load balancer is in front of Kong, this function
            returns the load balancer's address, and **not** that of the
            downstream client.

        Phases:
            certificate, rewrite, access, header_filter, response, body_filter, log

        Example:
            # Given a client with IP 127.0.0.1 making connection through

            # a load balancer with IP 10.0.0.1 to Kong answering the request for

            # https://example.com:1234/v1/movies

            kong.client.get_ip() # "10.0.0.1"

        :return: The remote IP address of the client making the request.

        :rtype: str
        """
        pass

    @staticmethod
    def get_port() -> number:
        """

            Returns the remote port of the client making the request. This
            **always** returns the port of the client directly connecting to Kong. That
            is, in cases when a load balancer is in front of Kong, this function
            returns the load balancer's port, and **not** that of the downstream client.

        Phases:
            certificate, rewrite, access, header_filter, response, body_filter, log

        Example:
            # [client]:40000 <-> 80:[balancer]:30000 <-> 80:[kong]:20000 <-> 80:[service]

            kong.client.get_port() # 30000

        :return: The remote client port.

        :rtype: number
        """
        pass

    @staticmethod
    def get_protocol(allow_terminated: Optional[bool]) -> Tuple[str, err]:
        """

            Returns the protocol matched by the current route (`"http"`, `"https"`, `"tcp"` or
            `"tls"`), or `nil`, if no route has been matched, which can happen when dealing with
            erroneous requests.

        Phases:
            access, header_filter, response, body_filter, log

        Example:
            kong.client.get_protocol() # "http"

        :parameter allow_terminated: If set, the `X-Forwarded-Proto` header is checked when checking for HTTPS.
        :type allow_terminated: bool

        :return: Can be one of `"http"`, `"https"`, `"tcp"`, `"tls"` or `nil`.

        :rtype: str
        :return: `nil` if successful, or an error message if it fails.

        :rtype: err
        """
        pass

    @staticmethod
    def load_consumer(consumer_id: str, search_by_username: Optional[bool]) -> Tuple[table, err]:
        """

            Returns the consumer from the datastore.
            Looks up the consumer by ID, and can optionally do a second search by name.

        Phases:
            access, header_filter, response, body_filter, log

        Example:
            consumer_id = "john_doe"

            consumer = kong.client.load_consumer(consumer_id, true)

        :parameter consumer_id: The consumer ID to look up.
        :type consumer_id: str
        :parameter search_by_username: If truthy,
            and if the consumer is not found by ID,
            then a second search by username will be performed.
        :type search_by_username: bool

        :return: Consumer entity or `nil`.

        :rtype: table
        :return: `nil` if successful, or an error message if it fails.

        :rtype: err
        """
        pass

    pass