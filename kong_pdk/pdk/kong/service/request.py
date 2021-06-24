# AUTO GENERATED BASED ON Kong 2.4.x, DO NOT EDIT
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
        kong.service.request.add_header("Cache-Control", "no-cache")
        kong.service.request.add_header("Cache-Control", "no-store")
        :param header: The header name. Example: "Cache-Control"
        :param value: The header value. Example: "no-cache"
        :returns throws an error on invalid inputs.
        """
        pass

    @staticmethod
    def clear_header(header: str) -> None:
        """
        kong.service.request.set_header("X-Foo", "foo")
        kong.service.request.add_header("X-Foo", "bar")
        kong.service.request.clear_header("X-Foo")
        -- from here onwards, no X-Foo headers will exist in the request
        :param header: The header name. Example: "X-Foo"
        :returns throws an error on invalid inputs.
        The function does not throw an error if no header was removed.
        """
        pass

    @staticmethod
    def disable_tls() -> Tuple[bool, str]:
        """
        local ok, err = kong.service.request.disable_tls()
        if not ok then
        -- do something with error
        end
        :returns `true` if the operation succeeded, `nil` if an error occurred
        returns An error message describing the error if there was one.
        """
        pass

    @staticmethod
    def enable_buffering() -> None:
        """
        kong.service.request.enable_buffering()
        :returns 
        """
        pass

    @staticmethod
    def set_body(args: table, mimetype: Optional[str]) -> Tuple[bool, str]:
        """
        kong.service.set_header("application/json")
        local ok, err = kong.service.request.set_body({
        name = "John Doe",
        age = 42,
        numbers = {1, 2, 3}
        })
        -- Produces the following JSON body:
        -- { "name": "John Doe", "age": 42, "numbers":[1, 2, 3] }
        local ok, err = kong.service.request.set_body({
        foo = "hello world",
        bar = {"baz", "bla", true},
        zzz = true,
        blo = ""
        }, "application/x-www-form-urlencoded")
        -- Produces the following body:
        -- bar=baz&bar=bla&bar&blo=&foo=hello%20world&zzz
        :param args: A table with data to be converted to the appropriate format
        and stored in the body.
        :param mimetype: can be one of:
        :returns `true` on success, `nil` otherwise
        returns `nil` on success, an error message in case of error.
        Throws an error on invalid inputs.
        """
        pass

    @staticmethod
    def set_header(header: str, value: Any) -> None:
        """
        kong.service.request.set_header("X-Foo", "value")
        :param header: The header name. Example: "X-Foo"
        :param value: The header value. Example: "hello world"
        :returns throws an error on invalid inputs.
        """
        pass

    @staticmethod
    def set_headers(headers: table) -> None:
        """
        kong.service.request.set_header("X-Foo", "foo1")
        kong.service.request.add_header("X-Foo", "foo2")
        kong.service.request.set_header("X-Bar", "bar1")
        kong.service.request.set_headers({
        ["X-Foo"] = "foo3",
        ["Cache-Control"] = { "no-store", "no-cache" },
        ["Bla"] = "boo"
        })
        -- Will add the following headers to the request, in this order:
        -- X-Bar: bar1
        -- Bla: boo
        -- Cache-Control: no-store
        -- Cache-Control: no-cache
        -- X-Foo: foo3
        :param headers: A table where each key is a string containing a header name
        and each value is either a string or an array of strings.
        :returns throws an error on invalid inputs.
        """
        pass

    @staticmethod
    def set_method(method: str) -> None:
        """
        kong.service.request.set_method("DELETE")
        :param method: The method string, which should be given in all
        uppercase. Supported values are: `"GET"`, `"HEAD"`, `"PUT"`, `"POST"`,
        `"DELETE"`, `"OPTIONS"`, `"MKCOL"`, `"COPY"`, `"MOVE"`, `"PROPFIND"`,
        `"PROPPATCH"`, `"LOCK"`, `"UNLOCK"`, `"PATCH"`, `"TRACE"`.
        :returns throws an error on invalid inputs.
        """
        pass

    @staticmethod
    def set_path(path: str) -> None:
        """
        kong.service.request.set_path("/v2/movies")
        :param path: The path string. Special characters and UTF-8 characters are allowed. Example: "/v2/movies" or "/foo/😀"
        :returns throws an error on invalid inputs.
        """
        pass

    @staticmethod
    def set_query(args: table) -> None:
        """
        kong.service.request.set_query({
        foo = "hello world",
        bar = {"baz", "bla", true},
        zzz = true,
        blo = ""
        })
        -- Will produce the following query string:
        -- bar=baz&bar=bla&bar&blo=&foo=hello%20world&zzz
        :param args: A table where each key is a string (corresponding to an
        argument name), and each value is either a boolean, a string or an array of
        strings or booleans. Any string values given are URL-encoded.
        :returns throws an error on invalid inputs.
        """
        pass

    @staticmethod
    def set_raw_body(body: str) -> None:
        """
        kong.service.request.set_raw_body("Hello, world!")
        :param body: The raw body
        :returns throws an error on invalid inputs.
        """
        pass

    @staticmethod
    def set_raw_query(query: str) -> None:
        """
        kong.service.request.set_raw_query("zzz&bar=baz&bar=bla&bar&blo=&foo=hello%20world")
        :param query: The raw querystring. Example: "foo=bar&bla&baz=hello%20world"
        :returns throws an error on invalid inputs.
        """
        pass

    @staticmethod
    def set_scheme(scheme: str) -> None:
        """
        kong.service.request.set_scheme("https")
        :param scheme: The scheme to be used. Supported values are `"http"` or `"https"`
        :returns throws an error on invalid inputs.
        """
        pass

    pass