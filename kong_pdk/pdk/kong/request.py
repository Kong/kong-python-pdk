# AUTO GENERATED BASED ON Kong 2.7.x, DO NOT EDIT
# Original source path: kong/pdk/request.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str


class request():


    @staticmethod
    def get_body(mimetype: Optional[str], max_args: Optional[number]) -> Tuple[table, str, str]:
        """
        local body, err, mimetype = kong.request.get_body()
        body.name -- "John Doe"
        body.age  -- "42"
        :param mimetype: The MIME type.
        :param max_args: Sets a limit on the maximum number of parsed
        arguments.
        :returns A table representation of the body.
        returns An error message.
        returns mimetype The MIME type used.
        """
        pass

    @staticmethod
    def get_forwarded_host() -> str:
        """
        kong.request.get_forwarded_host() -- "example.com"
        :returns The forwarded host.
        """
        pass

    @staticmethod
    def get_forwarded_path() -> str:
        """
        kong.request.get_forwarded_path() -- /path
        :returns The forwarded path.
        """
        pass

    @staticmethod
    def get_forwarded_port() -> number:
        """
        kong.request.get_forwarded_port() -- 1234
        :returns The forwarded port.
        """
        pass

    @staticmethod
    def get_forwarded_prefix() -> str:
        """
        kong.request.get_forwarded_prefix() -- /prefix
        :returns The forwarded path prefix or `nil` if the prefix was
        not stripped.
        """
        pass

    @staticmethod
    def get_forwarded_scheme() -> str:
        """
        kong.request.get_forwarded_scheme() -- "https"
        :returns The forwarded scheme.
        """
        pass

    @staticmethod
    def get_header(name: str) -> str:
        """
        -- Given a request with the following headers:
        -- Host: foo.com
        -- X-Custom-Header: bla
        -- X-Another: foo bar
        -- X-Another: baz
        kong.request.get_header("Host")            -- "foo.com"
        kong.request.get_header("x-custom-header") -- "bla"
        kong.request.get_header("X-Another")       -- "foo bar"
        :param name: the name of the header to be returned
        :returns the value of the header or nil if not present
        """
        pass

    @staticmethod
    def get_headers(max_headers: Optional[number]) -> table:
        """
        -- Given a request with the following headers:
        -- Host: foo.com
        -- X-Custom-Header: bla
        -- X-Another: foo bar
        -- X-Another: baz
        local headers = kong.request.get_headers()
        headers.host            -- "foo.com"
        headers.x_custom_header -- "bla"
        headers.x_another[1]    -- "foo bar"
        headers["X-Another"][2] -- "baz"
        :param max_headers: Sets a limit on the maximum number of
        parsed headers.
        :returns The request headers in table form.
        """
        pass

    @staticmethod
    def get_host() -> str:
        """
        -- Given a request to https://example.com:1234/v1/movies
        kong.request.get_host() -- "example.com"
        :returns The hostname.
        """
        pass

    @staticmethod
    def get_http_version() -> number:
        """
        kong.request.get_http_version() -- 1.1
        :returns The HTTP version as a Lua number.
        """
        pass

    @staticmethod
    def get_method() -> str:
        """
        kong.request.get_method() -- "GET"
        :returns The request method.
        """
        pass

    @staticmethod
    def get_path() -> str:
        """
        -- Given a request to https://example.com:1234/v1/movies?movie=foo
        kong.request.get_path() -- "/v1/movies"
        :returns The path.
        """
        pass

    @staticmethod
    def get_path_with_query() -> str:
        """
        -- Given a request to https://example.com:1234/v1/movies?movie=foo
        kong.request.get_path_with_query() -- "/v1/movies?movie=foo"
        :returns The path with the query string.
        """
        pass

    @staticmethod
    def get_port() -> number:
        """
        -- Given a request to https://example.com:1234/v1/movies
        kong.request.get_port() -- 1234
        :returns The port.
        """
        pass

    @staticmethod
    def get_query(max_args: Optional[number]) -> table:
        """
        -- Given a request GET /test?foo=hello%20world&bar=baz&zzz&blo=&bar=bla&bar
        for k, v in pairs(kong.request.get_query()) do
        kong.log.inspect(k, v)
        end
        -- Will print
        -- "foo" "hello world"
        -- "bar" {"baz", "bla", true}
        -- "zzz" true
        -- "blo" ""
        :param max_args: Sets a limit on the maximum number of parsed
        arguments.
        :returns A table representation of the query string.
        """
        pass

    @staticmethod
    def get_query_arg() -> Any:
        """
        -- Given a request GET /test?foo=hello%20world&bar=baz&zzz&blo=&bar=bla&bar
        kong.request.get_query_arg("foo") -- "hello world"
        kong.request.get_query_arg("bar") -- "baz"
        kong.request.get_query_arg("zzz") -- true
        kong.request.get_query_arg("blo") -- ""
        :returns The value of the argument.
        """
        pass

    @staticmethod
    def get_raw_body() -> str:
        """
        -- Given a body with payload "Hello, Earth!":
        kong.request.get_raw_body():gsub("Earth", "Mars") -- "Hello, Mars!"
        :returns The plain request body.
        """
        pass

    @staticmethod
    def get_raw_query() -> str:
        """
        -- Given a request to https://example.com/foo?msg=hello%20world&bla=&bar
        kong.request.get_raw_query() -- "msg=hello%20world&bla=&bar"
        :returns The query component of the request's URL.
        """
        pass

    @staticmethod
    def get_scheme() -> str:
        """
        -- Given a request to https://example.com:1234/v1/movies
        kong.request.get_scheme() -- "https"
        :returns A string like `"http"` or `"https"`.
        """
        pass

    pass