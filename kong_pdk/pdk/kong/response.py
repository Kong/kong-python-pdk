# AUTO GENERATED BASED ON Kong 2.4.x, DO NOT EDIT
# Original source path: kong/pdk/response.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str


class response():


    @staticmethod
    def add_header(name: str, value: Any) -> None:
        """
        kong.response.add_header("Cache-Control", "no-cache")
        kong.response.add_header("Cache-Control", "no-store")
        :param name: The header name
        :param value: The header value
        :returns throws an error on invalid input.
        """
        pass

    @staticmethod
    def clear_header(name: str) -> None:
        """
        kong.response.set_header("X-Foo", "foo")
        kong.response.add_header("X-Foo", "bar")
        kong.response.clear_header("X-Foo")
        -- from here onwards, no X-Foo headers will exist in the response
        :param name: The name of the header to be cleared
        :returns throws an error on invalid input.
        """
        pass

    @staticmethod
    def error(status: number, message: Optional[str], headers: Optional[table]) -> None:
        """
        return kong.response.error(403, "Access Forbidden", {
        ["Content-Type"] = "text/plain",
        ["WWW-Authenticate"] = "Basic"
        })
        ---
        return kong.response.error(403, "Access Forbidden")
        ---
        return kong.response.error(403)
        :param status: The status to be used (>399)
        :param message: The error message to be used
        :param headers: The headers to be used
        :returns throws an error on invalid input.
        """
        pass

    @staticmethod
    def exit(status: number, body: Optional[Any], headers: Optional[table]) -> None:
        """
        return kong.response.exit(403, "Access Forbidden", {
        ["Content-Type"] = "text/plain",
        ["WWW-Authenticate"] = "Basic"
        })
        ---
        return kong.response.exit(403, [[{"message":"Access Forbidden"}]], {
        ["Content-Type"] = "application/json",
        ["WWW-Authenticate"] = "Basic"
        })
        ---
        return kong.response.exit(403, { message = "Access Forbidden" }, {
        ["WWW-Authenticate"] = "Basic"
        })
        ---
        -- In L4 proxy mode
        return kong.response.exit(200, "Success")
        :param status: The status to be used
        :param body: The body to be used
        :param headers: The headers to be used
        :returns throws an error on invalid input.
        """
        pass

    @staticmethod
    def get_header(name: str) -> str:
        """
        -- Given a response with the following headers:
        -- X-Custom-Header: bla
        -- X-Another: foo bar
        -- X-Another: baz
        kong.response.get_header("x-custom-header") -- "bla"
        kong.response.get_header("X-Another")       -- "foo bar"
        kong.response.get_header("X-None")          -- nil
        :param name: The name of the header
        Header names are case-insensitive and dashes (`-`) can be written as
        underscores (`_`); that is, the header `X-Custom-Header` can also be
        retrieved as `x_custom_header`.
        :returns The value of the header
        """
        pass

    @staticmethod
    def get_headers(max_headers: Optional[number]) -> Tuple[table, str]:
        """
        -- Given an response from the Service with the following headers:
        -- X-Custom-Header: bla
        -- X-Another: foo bar
        -- X-Another: baz
        local headers = kong.response.get_headers()
        headers.x_custom_header -- "bla"
        headers.x_another[1]    -- "foo bar"
        headers["X-Another"][2] -- "baz"
        :param max_headers: Limits how many headers are parsed
        :returns headers A table representation of the headers in the
        response
        returns err If more headers than `max_headers` were present, a
        string with the error `"truncated"`.
        """
        pass

    @staticmethod
    def get_source() -> str:
        """
        if kong.response.get_source() == "service" then
        kong.log("The response comes from the Service")
        elseif kong.response.get_source() == "error" then
        kong.log("There was an error while processing the request")
        elseif kong.response.get_source() == "exit" then
        kong.log("There was an early exit while processing the request")
        end
        :returns the source.
        """
        pass

    @staticmethod
    def get_status() -> number:
        """
        kong.response.get_status() -- 200
        :returns status The HTTP status code currently set for the
        downstream response
        """
        pass

    @staticmethod
    def set_header(name: str, value: Any) -> None:
        """
        kong.response.set_header("X-Foo", "value")
        :param name: The name of the header
        :param value: The new value for the header
        :returns throws an error on invalid input.
        """
        pass

    @staticmethod
    def set_headers(headers: table) -> None:
        """
        kong.response.set_headers({
        ["Bla"] = "boo",
        ["X-Foo"] = "foo3",
        ["Cache-Control"] = { "no-store", "no-cache" }
        })
        -- Will add the following headers to the response, in this order:
        -- X-Bar: bar1
        -- Bla: boo
        -- Cache-Control: no-store
        -- Cache-Control: no-cache
        -- X-Foo: foo3
        :param headers: 
        :returns throws an error on invalid input.
        """
        pass

    @staticmethod
    def set_status(status: number) -> None:
        """
        kong.response.set_status(404)
        :param status: The new status
        :returns throws an error on invalid input.
        """
        pass

    pass