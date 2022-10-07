# AUTO GENERATED BASED ON Kong 3.1.x, DO NOT EDIT
# Original source path: kong/pdk/service/response.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str


class response():


    @staticmethod
    def get_body(mimetype: Optional[str], max_args: Optional[number]) -> str:
        """

            Returns the decoded buffered body.

        Phases:
            header_filter`, body_filter`, log`

        Example:
            # Plugin needs to call kong.service.request.enable_buffering() on `rewrite`

            # or `access` phase prior calling this function.

            body = kong.service.response.get_body()

        :parameter mimetype: The MIME type of the response (if known).
        :type mimetype: str
        :parameter max_args: Sets a limit on the maximum number of (what?)
            that can be parsed.
        :type max_args: number

        :return: The raw buffered body

        :rtype: str
        """
        pass

    @staticmethod
    def get_header(name: str) -> str:
        """

            Returns the value of the specified response header.
            Unlike `kong.response.get_header()`, this function only returns a header
            if it is present in the response from the Service (ignoring headers added by Kong
            itself).

        Phases:
            header_filter`, body_filter`, log`

        Example:
            # Given a response with the following headers:

            # X-Custom-Header: bla

            # X-Another: foo bar

            # X-Another: baz

            kong.log.inspect(kong.service.response.get_header("x-custom-header")) # "bla"

            kong.log.inspect(kong.service.response.get_header("X-Another"))       # "foo bar"

        :parameter name: The name of the header.
            Header names in are case-insensitive and are normalized to lowercase, and
            dashes (`-`) can be written as underscores (`_`); that is, the header
            `X-Custom-Header` can also be retrieved as `x_custom_header`.
        :type name: str

        :return: The value of the header, or `nil` if a header with
            `name` is not found in the response. If a header with the same name is present
            multiple times in the response, this function returns the value of the
            first occurrence of this header.

        :rtype: str
        """
        pass

    @staticmethod
    def get_headers(max_headers: Optional[number]) -> Tuple[table, str]:
        """

            Returns a Lua table holding the headers from the Service response. Keys are
            header names. Values are either a string with the header value, or an array of
            strings if a header was sent multiple times. Header names in this table are
            case-insensitive and dashes (`-`) can be written as underscores (`_`); that is,
            the header `X-Custom-Header` can also be retrieved as `x_custom_header`.
            Unlike `kong.response.get_headers()`, this function only returns headers that
            are present in the response from the Service (ignoring headers added by Kong itself).
            If the request is not proxied to a Service (e.g. an authentication plugin rejected
            a request and produced an HTTP 401 response), then the returned `headers` value
            might be `nil`, since no response from the Service has been received.
            By default, this function returns up to **100** headers. The optional
            `max_headers` argument can be specified to customize this limit, but must be
            greater than **1** and not greater than **1000**.

        Phases:
            header_filter`, body_filter`, log`

        Example:
            # Given a response with the following headers:

            # X-Custom-Header: bla

            # X-Another: foo bar

            # X-Another: baz

            headers = kong.service.response.get_headers()

            if headers:

                kong.log.inspect(headers.x_custom_header) # "bla"

            kong.log.inspect(headers.x_another[1])    # "foo bar"

            kong.log.inspect(headers["X-Another"][2]) # "baz"

        :parameter max_headers: Sets a limit on the maximum number of
            headers that can be parsed.
        :type max_headers: number

        :return: The response headers in table form.

        :rtype: table
        :return: If more headers than `max_headers` are present, returns
            a string with the error `"truncated"`.

        :rtype: str
        """
        pass

    @staticmethod
    def get_raw_body() -> bytes:
        """

            Returns the raw buffered body.

        Phases:
            header_filter`, body_filter`, log`

        Example:
            # Plugin needs to call kong.service.request.enable_buffering() on `rewrite`

            # or `access` phase prior calling this function.

            body = kong.service.response.get_raw_body()

        :return: The raw buffered body.

        :rtype: bytes
        """
        pass

    @staticmethod
    def get_status() -> number:
        """

            Returns the HTTP status code of the response from the Service as a Lua number.

        Phases:
            header_filter`, body_filter`, log`

        Example:
            kong.log.inspect(kong.service.response.get_status()) # 418

        :return: The status code from the response from the Service, or `nil`
            if the request was not proxied (that is, if `kong.response.get_source()` returned
            anything other than `"service"`).

        :rtype: number
        """
        pass

    pass