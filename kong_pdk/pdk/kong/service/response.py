# AUTO GENERATED BASED ON Kong 2.7.x, DO NOT EDIT
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
        -- Plugin needs to call kong.service.request.enable_buffering() on `rewrite`
        -- or `access` phase prior calling this function.
        local body = kong.service.response.get_body()
        :param mimetype: The MIME type of the response (if known).
        :param max_args: Sets a limit on the maximum number of (what?)
        that can be parsed.
        :returns The raw buffered body
        """
        pass

    @staticmethod
    def get_header(name: str) -> str:
        """
        -- Given a response with the following headers:
        -- X-Custom-Header: bla
        -- X-Another: foo bar
        -- X-Another: baz
        kong.log.inspect(kong.service.response.get_header("x-custom-header")) -- "bla"
        kong.log.inspect(kong.service.response.get_header("X-Another"))       -- "foo bar"
        :param name: The name of the header.
        Header names in are case-insensitive and are normalized to lowercase, and
        dashes (`-`) can be written as underscores (`_`); that is, the header
        `X-Custom-Header` can also be retrieved as `x_custom_header`.
        :returns The value of the header, or `nil` if a header with
        `name` is not found in the response. If a header with the same name is present
        multiple times in the response, this function returns the value of the
        first occurrence of this header.
        """
        pass

    @staticmethod
    def get_headers(max_headers: Optional[number]) -> Tuple[table, str]:
        """
        -- Given a response with the following headers:
        -- X-Custom-Header: bla
        -- X-Another: foo bar
        -- X-Another: baz
        local headers = kong.service.response.get_headers()
        if headers then
        kong.log.inspect(headers.x_custom_header) -- "bla"
        kong.log.inspect(headers.x_another[1])    -- "foo bar"
        kong.log.inspect(headers["X-Another"][2]) -- "baz"
        end
        :param max_headers: Sets a limit on the maximum number of
        headers that can be parsed.
        :returns The response headers in table form.
        returns If more headers than `max_headers` are present, returns
        a string with the error `"truncated"`.
        """
        pass

    @staticmethod
    def get_raw_body() -> str:
        """
        -- Plugin needs to call kong.service.request.enable_buffering() on `rewrite`
        -- or `access` phase prior calling this function.
        local body = kong.service.response.get_raw_body()
        :returns The raw buffered body.
        """
        pass

    @staticmethod
    def get_status() -> number:
        """
        kong.log.inspect(kong.service.response.get_status()) -- 418
        :returns The status code from the response from the Service, or `nil`
        if the request was not proxied (that is, if `kong.response.get_source()` returned
        anything other than `"service"`).
        """
        pass

    pass