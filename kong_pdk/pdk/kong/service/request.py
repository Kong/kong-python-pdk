# AUTO GENERATED BASED ON Kong 3.1.x, DO NOT EDIT
# Original source path: kong/pdk/service/request.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str


class request():


    @staticmethod
    def add_header(header: str, value: Any) -> None:
        """

            Adds a request header with the given value to the request to the Service. Unlike
            `kong.service.request.set_header()`, this function doesn't remove any existing
            headers with the same name. Instead, several occurrences of the header will be
            present in the request. The order in which headers are added is retained.

        Phases:
            rewrite`, access`

        Example:
            kong.service.request.add_header("Cache-Control", "no-cache")

            kong.service.request.add_header("Cache-Control", "no-store")

        :parameter header: The header name. Example: "Cache-Control".
        :type header: str
        :parameter value: The header value. Example: "no-cache".
        :type value: Any

        :return: throws an error on invalid inputs.

        :rtype: None
        """
        pass

    @staticmethod
    def clear_header(header: str) -> None:
        """

            Removes all occurrences of the specified header from the request to the Service.

        Phases:
            rewrite`, access`

        Example:
            kong.service.request.set_header("X-Foo", "foo")

            kong.service.request.add_header("X-Foo", "bar")

            kong.service.request.clear_header("X-Foo")

            # from here onwards, no X-Foo headers will exist in the request

        :parameter header: The header name. Example: "X-Foo".
        :type header: str

        :return: throws an error on invalid inputs.
            The function does not throw an error if no header was removed.

        :rtype: None
        """
        pass

    @staticmethod
    def disable_tls() -> Tuple[bool, str]:
        """

            Disables the TLS handshake to upstream for [ngx\_stream\_proxy\_module](https://nginx.org/en/docs/stream/ngx_stream_proxy_module.html).
            This overrides the [proxy\_ssl](https://nginx.org/en/docs/stream/ngx_stream_proxy_module.html#proxy_ssl) directive, effectively setting it to `off`
            for the current stream session.
            Once this function has been called, it is not possible to re-enable TLS handshake for the current session.

        Phases:
            preread`, balancer`

        Example:
            ok, err = kong.service.request.disable_tls()

            if not ok:

                # do something with error

        :return: `true` if the operation succeeded, `nil` if an error occurred.

        :rtype: bool
        :return: An error message describing the error if there was one.

        :rtype: str
        """
        pass

    @staticmethod
    def enable_buffering() -> None:
        """

            Enables buffered proxying, which allows plugins to access Service body and
            response headers at the same time.

        Phases:
            rewrite`, access`

        Example:
            kong.service.request.enable_buffering()

        :return: 

        :rtype: None
        """
        pass

    @staticmethod
    def set_body(args: table, mimetype: Optional[str]) -> Tuple[bool, str]:
        """

            Sets the body of the request to the Service. Unlike
            `kong.service.request.set_raw_body()`, the `args` argument must be a table, and
            is encoded with a MIME type.  The encoding MIME type can be specified in
            the optional `mimetype` argument, or if left unspecified, is chosen based
            on the `Content-Type` header of the client's request.
            Behavior based on MIME type in the `Content-Type` header:
            * `application/x-www-form-urlencoded`: Encodes the arguments as
              form-encoded. Keys are produced in lexicographical
              order. The order of entries within the same key (when values are
              given as an array) is retained. Any string values given are URL-encoded.
            * `multipart/form-data`: Encodes the arguments as multipart form data.
            * `application/json`: Encodes the arguments as JSON (same as
              `kong.service.request.set_raw_body(json.encode(args))`). Lua types are
              converted to matching JSON types.
            If the MIME type is none of the above, this function returns `nil` and
            an error message indicating the body could not be encoded.
            If the `mimetype` argument is specified, the `Content-Type` header is
            set accordingly in the request to the Service.
            If further control of the body generation is needed, a raw body can be given as
            a string with `kong.service.request.set_raw_body()`.

        Phases:
            rewrite`, access`

        Example:
            kong.service.set_header("application/json")

            ok, err = kong.service.request.set_body({

            name = "John Doe",

            age = 42,

            numbers = {1, 2, 3}

            })

            # Produces the following JSON body:

            # { "name": "John Doe", "age": 42, "numbers":[1, 2, 3] }

            ok, err = kong.service.request.set_body({

            foo = "hello world",

            bar = {"baz", "bla", true},

            zzz = true,

            blo = ""

            }, "application/x-www-form-urlencoded")

            # Produces the following body:

            # bar=baz&bar=bla&bar&blo=&foo=hello%20world&zzz

        :parameter args: A table with data to be converted to the appropriate format
            and stored in the body.
        :type args: table
        :parameter mimetype: can be one of:
        :type mimetype: str

        :return: `true` on success, `nil` otherwise.

        :rtype: bool
        :return: `nil` on success, an error message in case of error.
            Throws an error on invalid inputs.

        :rtype: str
        """
        pass

    @staticmethod
    def set_header(header: str, value: Any) -> None:
        """

            Sets a header in the request to the Service with the given value. Any existing header
            with the same name will be overridden.
            If the `header` argument is `"host"` (case-insensitive), then this also
            sets the SNI of the request to the Service.

        Phases:
            rewrite`, access`, balancer`

        Example:
            kong.service.request.set_header("X-Foo", "value")

        :parameter header: The header name. Example: "X-Foo".
        :type header: str
        :parameter value: The header value. Example: "hello world".
        :type value: Any

        :return: throws an error on invalid inputs.

        :rtype: None
        """
        pass

    @staticmethod
    def set_headers(headers: table) -> None:
        """

            Sets the headers of the request to the Service. Unlike
            `kong.service.request.set_header()`, the `headers` argument must be a table in
            which each key is a string (corresponding to a header's name), and each value
            is a string, or an array of strings.
            The resulting headers are produced in lexicographical order. The order of
            entries with the same name (when values are given as an array) is retained.
            This function overrides any existing header bearing the same name as those
            specified in the `headers` argument. Other headers remain unchanged.
            If the `"Host"` header is set (case-insensitive), then this also sets
            the SNI of the request to the Service.

        Phases:
            rewrite`, access`

        Example:
            kong.service.request.set_header("X-Foo", "foo1")

            kong.service.request.add_header("X-Foo", "foo2")

            kong.service.request.set_header("X-Bar", "bar1")

            kong.service.request.set_headers({

            ["X-Foo"] = "foo3",

            ["Cache-Control"] = { "no-store", "no-cache" },

            ["Bla"] = "boo"

            })

            # Will add the following headers to the request, in this order:

            # X-Bar: bar1

            # Bla: boo

            # Cache-Control: no-store

            # Cache-Control: no-cache

            # X-Foo: foo3

        :parameter headers: A table where each key is a string containing a header name
            and each value is either a string or an array of strings.
        :type headers: table

        :return: throws an error on invalid inputs.

        :rtype: None
        """
        pass

    @staticmethod
    def set_method(method: str) -> None:
        """

            Sets the HTTP method for the request to the service.

        Phases:
            rewrite`, access`

        Example:
            kong.service.request.set_method("DELETE")

        :parameter method: The method string, which must be in all
            uppercase. Supported values are: `"GET"`, `"HEAD"`, `"PUT"`, `"POST"`,
            `"DELETE"`, `"OPTIONS"`, `"MKCOL"`, `"COPY"`, `"MOVE"`, `"PROPFIND"`,
            `"PROPPATCH"`, `"LOCK"`, `"UNLOCK"`, `"PATCH"`, or `"TRACE"`.
        :type method: str

        :return: throws an error on invalid inputs.

        :rtype: None
        """
        pass

    @staticmethod
    def set_path(path: str) -> None:
        """

            Sets the path component for the request to the service.
            The input accepts any valid *normalized* URI (including UTF-8 characters)
            and this API will perform necessary escaping according to the RFC
            to make the request valid.
            Input should **not** include the query string.

        Phases:
            access`

        Example:
            kong.service.request.set_path("/v2/movies")

        :parameter path: The path string. Special characters and UTF-8
            characters are allowed, for example: `"/v2/movies"` or `"/foo/😀"`.
        :type path: str

        :return: throws an error on invalid inputs.

        :rtype: None
        """
        pass

    @staticmethod
    def set_query(args: table) -> None:
        """

            Set the query string of the request to the Service.
            Unlike `kong.service.request.set_raw_query()`, the `query` argument must be a
            table in which each key is a string (corresponding to an argument's name), and
            each value is either a boolean, a string, or an array of strings or booleans.
            Additionally, all string values will be URL-encoded.
            The resulting query string contains keys in their lexicographical order. The
            order of entries within the same key (when values are given as an array) is
            retained.
            If further control of the query string generation is needed, a raw query
            string can be given as a string with `kong.service.request.set_raw_query()`.

        Phases:
            rewrite`, access`

        Example:
            kong.service.request.set_query({

            foo = "hello world",

            bar = {"baz", "bla", true},

            zzz = true,

            blo = ""

            })

            # Produces the following query string:

            # bar=baz&bar=bla&bar&blo=&foo=hello%20world&zzz

        :parameter args: A table where each key is a string (corresponding to an
            argument name), and each value is either a boolean, a string, or an array of
            strings or booleans. Any string values given are URL-encoded.
        :type args: table

        :return: throws an error on invalid inputs.

        :rtype: None
        """
        pass

    @staticmethod
    def set_raw_body(body: str) -> None:
        """

            Sets the body of the request to the Service.
            The `body` argument must be a string and will not be processed in any way.
            This function also sets the `Content-Length` header appropriately. To set an
            empty body, you can provide an empty string (`""`) to this function.
            For a higher-level function to set the body based on the request content type,
            see `kong.service.request.set_body()`.

        Phases:
            rewrite`, access`

        Example:
            kong.service.request.set_raw_body("Hello, world!")

        :parameter body: The raw body.
        :type body: str

        :return: throws an error on invalid inputs.

        :rtype: None
        """
        pass

    @staticmethod
    def set_raw_query(query: str) -> None:
        """

            Sets the query string of the request to the Service. The `query` argument is a
            string (without the leading `?` character), and is not processed in any
            way.
            For a higher-level function to set the query string from a Lua table of
            arguments, see `kong.service.request.set_query()`.

        Phases:
            rewrite`, access`

        Example:
            kong.service.request.set_raw_query("zzz&bar=baz&bar=bla&bar&blo=&foo=hello%20world")

        :parameter query: The raw querystring. Example:
            `"foo=bar&bla&baz=hello%20world"`.
        :type query: str

        :return: throws an error on invalid inputs.

        :rtype: None
        """
        pass

    @staticmethod
    def set_scheme(scheme: str) -> None:
        """

            Sets the protocol to use when proxying the request to the Service.

        Phases:
            access`

        Example:
            kong.service.request.set_scheme("https")

        :parameter scheme: The scheme to be used. Supported values are `"http"` or `"https"`.
        :type scheme: str

        :return: throws an error on invalid inputs.

        :rtype: None
        """
        pass

    pass