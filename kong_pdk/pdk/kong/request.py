# AUTO GENERATED BASED ON Kong 3.1.x, DO NOT EDIT
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

            Returns the request data as a key/value table.
            A high-level convenience function.
            The body is parsed with the most appropriate format:
            * If `mimetype` is specified, it decodes the body with the requested
              content type (if supported). This takes precedence over any content type
              present in the request.
              The optional argument `mimetype` can be one of the following strings:
                * `application/x-www-form-urlencoded`
                * `application/json`
                * `multipart/form-data`
            Whether `mimetype` is specified or a request content type is otherwise
            present in the request, each content type behaves as follows:
            * If the request content type is `application/x-www-form-urlencoded`:
              * Returns the body as form-encoded.
            * If the request content type is `multipart/form-data`:
              * Decodes the body as multipart form data
                (same as `multipart(kong.request.get_raw_body(),
                kong.request.get_header("Content-Type")):get_all()` ).
            * If the request content type is `application/json`:
              * Decodes the body as JSON
                (same as `json.decode(kong.request.get_raw_body())`).
              * JSON types are converted to matching Lua types.
            * If the request contains none of the above and the `mimetype` argument is
              not set, returns `nil` and an error message indicating the
              body could not be parsed.
            The optional argument `max_args` can be used to set a limit on the number
            of form arguments parsed for `application/x-www-form-urlencoded` payloads.
            The third return value is string containing the mimetype used to parsed
            the body (as per the `mimetype` argument), allowing the caller to identify
            what MIME type the body was parsed as.

        Phases:
            rewrite, access, response, admin_api

        Example:
            body, err, mimetype = kong.request.get_body()

            body.name # "John Doe"

            body.age  # "42"

        :parameter mimetype: The MIME type.
        :type mimetype: str
        :parameter max_args: Sets a limit on the maximum number of parsed
            arguments.
        :type max_args: number

        :return: A table representation of the body.

        :rtype: table
        :return: An error message.

        :rtype: str
        :return: mimetype The MIME type used.

        :rtype: str
        """
        pass

    @staticmethod
    def get_forwarded_host() -> str:
        """

            Returns the host component of the request's URL or the value of the "host"
            header. Unlike `kong.request.get_host()`, this function also considers
            `X-Forwarded-Host` if it comes from a trusted source. The returned value
            is normalized to lowercase.
            Whether this function considers `X-Forwarded-Host` or not depends on
            several Kong configuration parameters:
            * [trusted\_ips](https://docs.konghq.com/gateway/latest/reference/configuration/#trusted_ips)
            * [real\_ip\_header](https://docs.konghq.com/gateway/latest/reference/configuration/#real_ip_header)
            * [real\_ip\_recursive](https://docs.konghq.com/gateway/latest/reference/configuration/#real_ip_recursive)
            **Note**: Kong does not offer support for the Forwarded HTTP Extension
            (RFC 7239) since it is not supported by ngx_http_realip_module.

        Phases:
            rewrite, access, header_filter, response, body_filter, log, admin_api

        Example:
            kong.request.get_forwarded_host() # "example.com"

        :return: The forwarded host.

        :rtype: str
        """
        pass

    @staticmethod
    def get_forwarded_path() -> str:
        """

            Returns the path component of the request's URL, but also considers
            `X-Forwarded-Path` if it comes from a trusted source. The value
            is returned as a Lua string.
            Whether this function considers `X-Forwarded-Path` or not depends on
            several Kong configuration parameters:
            * [trusted\_ips](https://docs.konghq.com/gateway/latest/reference/configuration/#trusted_ips)
            * [real\_ip\_header](https://docs.konghq.com/gateway/latest/reference/configuration/#real_ip_header)
            * [real\_ip\_recursive](https://docs.konghq.com/gateway/latest/reference/configuration/#real_ip_recursive)
            **Note**: Kong does not do any normalization on the request path.

        Phases:
            rewrite, access, header_filter, response, body_filter, log, admin_api

        Example:
            kong.request.get_forwarded_path() # /path

        :return: The forwarded path.

        :rtype: str
        """
        pass

    @staticmethod
    def get_forwarded_port() -> number:
        """

            Returns the port component of the request's URL, but also considers
            `X-Forwarded-Host` if it comes from a trusted source. The value
            is returned as a Lua number.
            Whether this function considers `X-Forwarded-Proto` or not depends on
            several Kong configuration parameters:
            * [trusted\_ips](https://docs.konghq.com/gateway/latest/reference/configuration/#trusted_ips)
            * [real\_ip\_header](https://docs.konghq.com/gateway/latest/reference/configuration/#real_ip_header)
            * [real\_ip\_recursive](https://docs.konghq.com/gateway/latest/reference/configuration/#real_ip_recursive)
            **Note**: Kong does not offer support for the Forwarded HTTP Extension
            (RFC 7239) since it is not supported by ngx_http_realip_module.
            When running Kong behind the L4 port mapping (or forwarding), you can also
            configure:
            * [port\_maps](https://docs.konghq.com/gateway/latest/reference/configuration/#port_maps)
            The `port_maps` configuration parameter enables this function to return the
            port to which the port Kong is listening to is mapped to (in case they differ).

        Phases:
            rewrite, access, header_filter, response, body_filter, log, admin_api

        Example:
            kong.request.get_forwarded_port() # 1234

        :return: The forwarded port.

        :rtype: number
        """
        pass

    @staticmethod
    def get_forwarded_prefix() -> str:
        """

            Returns the prefix path component of the request's URL that Kong stripped
            before proxying to upstream. It also checks if `X-Forwarded-Prefix` comes
            from a trusted source, and uses it as-is when given. The value is returned
            as a Lua string.
            If a trusted `X-Forwarded-Prefix` is not passed, this function must be
            called after Kong has run its router (`access` phase),
            as the Kong router may strip the prefix of the request path. That stripped
            path becomes the return value of this function, unless there is already
            a trusted `X-Forwarded-Prefix` header in the request.
            Whether this function considers `X-Forwarded-Prefix` or not depends on
            several Kong configuration parameters:
            * [trusted\_ips](https://docs.konghq.com/gateway/latest/reference/configuration/#trusted_ips)
            * [real\_ip\_header](https://docs.konghq.com/gateway/latest/reference/configuration/#real_ip_header)
            * [real\_ip\_recursive](https://docs.konghq.com/gateway/latest/reference/configuration/#real_ip_recursive)
            **Note**: Kong does not do any normalization on the request path prefix.

        Phases:
            rewrite, access, header_filter, response, body_filter, log, admin_api

        Example:
            kong.request.get_forwarded_prefix() # /prefix

        :return: The forwarded path prefix or `nil` if the prefix was
            not stripped.

        :rtype: str
        """
        pass

    @staticmethod
    def get_forwarded_scheme() -> str:
        """

            Returns the scheme component of the request's URL, but also considers
            `X-Forwarded-Proto` if it comes from a trusted source. The returned
            value is normalized to lowercase.
            Whether this function considers `X-Forwarded-Proto` or not depends on
            several Kong configuration parameters:
            * [trusted\_ips](https://docs.konghq.com/gateway/latest/reference/configuration/#trusted_ips)
            * [real\_ip\_header](https://docs.konghq.com/gateway/latest/reference/configuration/#real_ip_header)
            * [real\_ip\_recursive](https://docs.konghq.com/gateway/latest/reference/configuration/#real_ip_recursive)
            **Note**: Kong does not offer support for the Forwarded HTTP Extension
            (RFC 7239) since it is not supported by ngx_http_realip_module.

        Phases:
            rewrite, access, header_filter, response, body_filter, log, admin_api

        Example:
            kong.request.get_forwarded_scheme() # "https"

        :return: The forwarded scheme.

        :rtype: str
        """
        pass

    @staticmethod
    def get_header(name: str) -> str:
        """

            Returns the value of the specified request header.
            The returned value is either a `string`, or can be `nil` if a header with
            `name` was not found in the request. If a header with the same name is
            present multiple times in the request, this function returns the value
            of the first occurrence of this header.
            Header names in are case-insensitive and are normalized to lowercase, and
            dashes (`-`) can be written as underscores (`_`); that is, the header
            `X-Custom-Header` can also be retrieved as `x_custom_header`.

        Phases:
            rewrite, access, header_filter, response, body_filter, log, admin_api

        Example:
            # Given a request with the following headers:

            # Host: foo.com

            # X-Custom-Header: bla

            # X-Another: foo bar

            # X-Another: baz

            kong.request.get_header("Host")            # "foo.com"

            kong.request.get_header("x-custom-header") # "bla"

            kong.request.get_header("X-Another")       # "foo bar"

        :parameter name: the name of the header to be returned
        :type name: str

        :return: the value of the header or nil if not present

        :rtype: str
        """
        pass

    @staticmethod
    def get_headers(max_headers: Optional[number]) -> table:
        """

            Returns a Lua table holding the request headers. Keys are header names.
            Values are either a string with the header value, or an array of strings
            if a header was sent multiple times. Header names in this table are
            case-insensitive and are normalized to lowercase, and dashes (`-`) can be
            written as underscores (`_`); that is, the header `X-Custom-Header` can
            also be retrieved as `x_custom_header`.
            By default, this function returns up to **100** headers. The optional
            `max_headers` argument can be specified to customize this limit, but must
            be greater than **1** and not greater than **1000**.

        Phases:
            rewrite, access, header_filter, response, body_filter, log, admin_api

        Example:
            # Given a request with the following headers:

            # Host: foo.com

            # X-Custom-Header: bla

            # X-Another: foo bar

            # X-Another: baz

            headers = kong.request.get_headers()

            headers.host            # "foo.com"

            headers.x_custom_header # "bla"

            headers.x_another[1]    # "foo bar"

            headers["X-Another"][2] # "baz"

        :parameter max_headers: Sets a limit on the maximum number of
            parsed headers.
        :type max_headers: number

        :return: The request headers in table form.

        :rtype: table
        """
        pass

    @staticmethod
    def get_host() -> str:
        """

            Returns the host component of the request's URL, or the value of the
            "Host" header. The returned value is normalized to lowercase form.

        Phases:
            rewrite, access, header_filter, response, body_filter, log, admin_api

        Example:
            # Given a request to https://example.com:1234/v1/movies

            kong.request.get_host() # "example.com"

        :return: The hostname.

        :rtype: str
        """
        pass

    @staticmethod
    def get_http_version() -> number:
        """

            Returns the HTTP version used by the client in the request as a Lua
            number, returning values such as `1`, `1.1`, `2.0`, or `nil` for
            unrecognized values.

        Phases:
            rewrite, access, header_filter, response, body_filter, log, admin_api

        Example:
            kong.request.get_http_version() # 1.1

        :return: The HTTP version as a Lua number.

        :rtype: number
        """
        pass

    @staticmethod
    def get_method() -> str:
        """

            Returns the HTTP method of the request. The value is normalized to
            uppercase.

        Phases:
            rewrite, access, header_filter, response, body_filter, log, admin_api

        Example:
            kong.request.get_method() # "GET"

        :return: The request method.

        :rtype: str
        """
        pass

    @staticmethod
    def get_path() -> str:
        """

            Returns the normalized path component of the request's URL. The return
            value is the same as `kong.request.get_raw_path()` but normalized according
            to RFC 3986 section 6:
            * Percent-encoded values of unreserved characters are decoded (`%20`
              becomes ` `).
            * Percent-encoded values of reserved characters have their hexidecimal
              value uppercased (`%2f` becomes `%2F`).
            * Relative path elements (`/.` and `/..`) are dereferenced.
            * Duplicate slashes are consolidated (`//` becomes `/`).

        Phases:
            rewrite, access, header_filter, response, body_filter, log, admin_api

        Example:
            # Given a request to https://example.com/t/Abc%20123%C3%B8%2f/parent/..//test/./

            kong.request.get_path() # "/t/Abc 123ø%2F/test/"

        :return: the path

        :rtype: str
        """
        pass

    @staticmethod
    def get_path_with_query() -> str:
        """

            Returns the path, including the query string if any. No
            transformations or normalizations are done.

        Phases:
            rewrite, access, header_filter, response, body_filter, log, admin_api

        Example:
            # Given a request to https://example.com:1234/v1/movies?movie=foo

            kong.request.get_path_with_query() # "/v1/movies?movie=foo"

        :return: The path with the query string.

        :rtype: str
        """
        pass

    @staticmethod
    def get_port() -> number:
        """

            Returns the port component of the request's URL. The value is returned
            as a Lua number.

        Phases:
            certificate, rewrite, access, header_filter, response, body_filter, log, admin_api

        Example:
            # Given a request to https://example.com:1234/v1/movies

            kong.request.get_port() # 1234

        :return: The port.

        :rtype: number
        """
        pass

    @staticmethod
    def get_query(max_args: Optional[number]) -> table:
        """

            Returns the table of query arguments obtained from the query string. Keys
            are query argument names. Values are either a string with the argument
            value, a boolean `true` if an argument was not given a value, or an array
            if an argument was given in the query string multiple times. Keys and
            values are unescaped according to URL-encoded escaping rules.
            Note that a query string `?foo&bar` translates to two boolean `true`
            arguments, and `?foo=&bar=` translates to two string arguments containing
            empty strings.
            By default, this function returns up to **100** arguments. The optional
            `max_args` argument can be specified to customize this limit, but must be
            greater than **1** and not greater than **1000**.

        Phases:
            rewrite, access, header_filter, response, body_filter, log, admin_api

        Example:
            # Given a request GET /test?foo=hello%20world&bar=baz&zzz&blo=&bar=bla&bar

            for k, v in pairs(kong.request.get_query()) do

            kong.log.inspect(k, v)# Will print

            # "foo" "hello world"

            # "bar" {"baz", "bla", true}

            # "zzz" true

            # "blo" ""

        :parameter max_args: Sets a limit on the maximum number of parsed
            arguments.
        :type max_args: number

        :return: A table representation of the query string.

        :rtype: table
        """
        pass

    @staticmethod
    def get_query_arg() -> Any:
        """

            Returns the value of the specified argument, obtained from the query
            arguments of the current request.
            The returned value is either a `string`, a boolean `true` if an
            argument was not given a value, or `nil` if no argument with `name` was
            found.
            If an argument with the same name is present multiple times in the
            query string, this function returns the value of the first occurrence.

        Phases:
            rewrite, access, header_filter, response, body_filter, log, admin_api

        Example:
            # Given a request GET /test?foo=hello%20world&bar=baz&zzz&blo=&bar=bla&bar

            kong.request.get_query_arg("foo") # "hello world"

            kong.request.get_query_arg("bar") # "baz"

            kong.request.get_query_arg("zzz") # true

            kong.request.get_query_arg("blo") # ""

        :return: The value of the argument.

        :rtype: Any
        """
        pass

    @staticmethod
    def get_raw_body() -> bytes:
        """

            Returns the plain request body.
            If the body has no size (empty), this function returns an empty string.
            If the size of the body is greater than the Nginx buffer size (set by
            `client_body_buffer_size`), this function fails and returns an error
            message explaining this limitation.

        Phases:
            rewrite, access, response, admin_api

        Example:
            # Given a body with payload "Hello, Earth!":

            kong.request.get_raw_body():gsub("Earth", "Mars") # "Hello, Mars!"

        :return: The plain request body.

        :rtype: bytes
        """
        pass

    @staticmethod
    def get_raw_path() -> str:
        """

            Returns the path component of the request's URL. It is not normalized in
            any way and does not include the query string.
            **NOTE:** Using the raw path to perform string comparision during request
            handling (such as in routing, ACL/authorization checks, setting rate-limit
            keys, etc) is widely regarded as insecure, as it can leave plugin code
            vulnerable to path traversal attacks. Prefer `kong.request.get_path()` for
            such use cases.

        Phases:
            rewrite, access, header_filter, response, body_filter, log, admin_api

        Example:
            # Given a request to https://example.com/t/Abc%20123%C3%B8%2f/parent/..//test/./?movie=foo

            kong.request.get_raw_path() # "/t/Abc%20123%C3%B8%2f/parent/..//test/./"

        :return: The path.

        :rtype: str
        """
        pass

    @staticmethod
    def get_raw_query() -> str:
        """

            Returns the query component of the request's URL. It is not normalized in
            any way (not even URL-decoding of special characters) and does not
            include the leading `?` character.

        Phases:
            rewrite, access, header_filter, response, body_filter, log, admin_api

        Example:
            # Given a request to https://example.com/foo?msg=hello%20world&bla=&bar

            kong.request.get_raw_query() # "msg=hello%20world&bla=&bar"

        :return: The query component of the request's URL.

        :rtype: str
        """
        pass

    @staticmethod
    def get_scheme() -> str:
        """

            Returns the scheme component of the request's URL. The returned value is
            normalized to lowercase form.

        Phases:
            rewrite, access, header_filter, response, body_filter, log, admin_api

        Example:
            # Given a request to https://example.com:1234/v1/movies

            kong.request.get_scheme() # "https"

        :return: A string like `"http"` or `"https"`.

        :rtype: str
        """
        pass

    @staticmethod
    def get_start_time() -> number:
        """

            Returns the request start time, in Unix epoch milliseconds.

        Phases:
            rewrite, access, header_filter, response, body_filter, log, admin_api

        Example:
            kong.request.get_start_time() # 1649960273000

        :return: The timestamp

        :rtype: number
        """
        pass

    @staticmethod
    def get_uri_captures() -> table:
        """

            Returns the URI captures matched by the router.

        Phases:
            rewrite, access, header_filter, response, body_filter, log, admin_api

        Example:
            captures = kong.request.get_uri_captures()

            for idx, value in ipairs(captures.unnamed) do

            # do what you want to capturesfor name, value in pairs(captures.named) do

            # do what you want to captures

        :return: tables containing unamed and named captures.

        :rtype: table
        """
        pass

    pass