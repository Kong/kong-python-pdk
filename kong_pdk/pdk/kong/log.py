# AUTO GENERATED BASED ON Kong 3.1.x, DO NOT EDIT
# Original source path: kong/pdk/log.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str


class log():


    @staticmethod
    def alert(*args: Any) -> None:
        """

            Similar to `kong.log()`, but the produced log has the severity given by
            `<level>`, instead of `notice`. The supported levels are:
            * `kong.log.alert()`
            * `kong.log.crit()`
            * `kong.log.err()`
            * `kong.log.warn()`
            * `kong.log.notice()`
            * `kong.log.info()`
            * `kong.log.debug()`
            Logs have the same format as that of `kong.log()`. For
            example, the following call:
            ``` lua
             kong.log.err("hello ", "world")
            ```
            would, within the core, produce a log line similar to:
            ``` plain
            2017/07/09 19:36:25 [error] 25932#0: *1 [kong] some_file.lua:54 hello world, client: 127.0.0.1, server: localhost, request: "GET /log HTTP/1.1", host: "localhost"
            ```
            If invoked from within a plugin (for example, `key-auth`) it would include the
            namespace prefix:
            ``` plain
            2017/07/09 19:36:25 [error] 25932#0: *1 [kong] some_file.lua:54 [key-auth] hello world, client: 127.0.0.1, server: localhost, request: "GET /log HTTP/1.1", host: "localhost"
            ```

        Phases:
            init_worker, certificate, rewrite, access, header_filter, response, body_filter, log

        Example:
            kong.log.warn("something require attention")

            kong.log.err("something failed: ", err)

            kong.log.alert("something requires immediate action")

        :parameter *args: All params will be concatenated and stringified before being sent to the log.
        :type *args: Any

        :return: Throws an error on invalid inputs.

        :rtype: None
        """
        pass

    @staticmethod
    def crit(*args: Any) -> None:
        """

            Similar to `kong.log()`, but the produced log has the severity given by
            `<level>`, instead of `notice`. The supported levels are:
            * `kong.log.alert()`
            * `kong.log.crit()`
            * `kong.log.err()`
            * `kong.log.warn()`
            * `kong.log.notice()`
            * `kong.log.info()`
            * `kong.log.debug()`
            Logs have the same format as that of `kong.log()`. For
            example, the following call:
            ``` lua
             kong.log.err("hello ", "world")
            ```
            would, within the core, produce a log line similar to:
            ``` plain
            2017/07/09 19:36:25 [error] 25932#0: *1 [kong] some_file.lua:54 hello world, client: 127.0.0.1, server: localhost, request: "GET /log HTTP/1.1", host: "localhost"
            ```
            If invoked from within a plugin (for example, `key-auth`) it would include the
            namespace prefix:
            ``` plain
            2017/07/09 19:36:25 [error] 25932#0: *1 [kong] some_file.lua:54 [key-auth] hello world, client: 127.0.0.1, server: localhost, request: "GET /log HTTP/1.1", host: "localhost"
            ```

        Phases:
            init_worker, certificate, rewrite, access, header_filter, response, body_filter, log

        Example:
            kong.log.warn("something require attention")

            kong.log.err("something failed: ", err)

            kong.log.alert("something requires immediate action")

        :parameter *args: All params will be concatenated and stringified before being sent to the log.
        :type *args: Any

        :return: Throws an error on invalid inputs.

        :rtype: None
        """
        pass

    @staticmethod
    def debug(*args: Any) -> None:
        """

            Similar to `kong.log()`, but the produced log has the severity given by
            `<level>`, instead of `notice`. The supported levels are:
            * `kong.log.alert()`
            * `kong.log.crit()`
            * `kong.log.err()`
            * `kong.log.warn()`
            * `kong.log.notice()`
            * `kong.log.info()`
            * `kong.log.debug()`
            Logs have the same format as that of `kong.log()`. For
            example, the following call:
            ``` lua
             kong.log.err("hello ", "world")
            ```
            would, within the core, produce a log line similar to:
            ``` plain
            2017/07/09 19:36:25 [error] 25932#0: *1 [kong] some_file.lua:54 hello world, client: 127.0.0.1, server: localhost, request: "GET /log HTTP/1.1", host: "localhost"
            ```
            If invoked from within a plugin (for example, `key-auth`) it would include the
            namespace prefix:
            ``` plain
            2017/07/09 19:36:25 [error] 25932#0: *1 [kong] some_file.lua:54 [key-auth] hello world, client: 127.0.0.1, server: localhost, request: "GET /log HTTP/1.1", host: "localhost"
            ```

        Phases:
            init_worker, certificate, rewrite, access, header_filter, response, body_filter, log

        Example:
            kong.log.warn("something require attention")

            kong.log.err("something failed: ", err)

            kong.log.alert("something requires immediate action")

        :parameter *args: All params will be concatenated and stringified before being sent to the log.
        :type *args: Any

        :return: Throws an error on invalid inputs.

        :rtype: None
        """
        pass

    @staticmethod
    def deprecation(*args: Any) -> None:
        """

            Arguments given to this function can be of any type, but table arguments
            are converted to strings via `tostring` (thus potentially calling a
            table's `__tostring` metamethod if set). When the last argument is a table,
            it is considered as a deprecation metadata. The table can include the
            following properties:
            ``` lua
            {
              after = "2.5.0",   -- deprecated after Kong version 2.5.0 (defaults to `nil`)
              removal = "3.0.0", -- about to be removed with Kong version 3.0.0 (defaults to `nil`)
              trace = true,      -- writes stack trace along with the deprecation message (defaults to `nil`)
            }
            ```
            For example, the following call:
            ``` lua
            kong.log.deprecation("hello ", "world")
            ```
            would, within the core, produce a log line similar to:
            ``` plain
            2017/07/09 19:36:25 [warn] 25932#0: *1 [kong] some_file.lua:54 hello world, client: 127.0.0.1, server: localhost, request: "GET /log HTTP/1.1", host: "localhost"
            ```
            If invoked from within a plugin (for example, `key-auth`) it would include the
            namespace prefix:
            ``` plain
            2017/07/09 19:36:25 [warn] 25932#0: *1 [kong] some_file.lua:54 [key-auth] hello world, client: 127.0.0.1, server: localhost, request: "GET /log HTTP/1.1", host: "localhost"
            ```
            And with metatable, the following call:
            ``` lua
            kong.log.deprecation("hello ", "world", { after = "2.5.0", removal = "3.0.0" })
            ```
            would, within the core, produce a log line similar to:
            ``` plain
            2017/07/09 19:36:25 [warn] 25932#0: *1 [kong] some_file.lua:54 hello world (deprecated after 2.5.0, scheduled for removal in 3.0.0), client: 127.0.0.1, server: localhost, request: "GET /log HTTP/1.1", host: "localhost"
            ```

        Phases:
            init_worker, certificate, rewrite, access, header_filter, response, body_filter, log

        Example:
            kong.log.deprecation("hello ", "world")

            kong.log.deprecation("hello ", "world", { after = "2.5.0" })

            kong.log.deprecation("hello ", "world", { removal = "3.0.0" })

            kong.log.deprecation("hello ", "world", { after = "2.5.0", removal = "3.0.0" })

            kong.log.deprecation("hello ", "world", { trace = true })

        :parameter *args: all params will be concatenated and stringified before being sent to the log
            (if the last param is a table, it is considered as a deprecation metadata)
        :type *args: Any

        :return: throws an error on invalid inputs.

        :rtype: None
        """
        pass

    @staticmethod
    def err(*args: Any) -> None:
        """

            Similar to `kong.log()`, but the produced log has the severity given by
            `<level>`, instead of `notice`. The supported levels are:
            * `kong.log.alert()`
            * `kong.log.crit()`
            * `kong.log.err()`
            * `kong.log.warn()`
            * `kong.log.notice()`
            * `kong.log.info()`
            * `kong.log.debug()`
            Logs have the same format as that of `kong.log()`. For
            example, the following call:
            ``` lua
             kong.log.err("hello ", "world")
            ```
            would, within the core, produce a log line similar to:
            ``` plain
            2017/07/09 19:36:25 [error] 25932#0: *1 [kong] some_file.lua:54 hello world, client: 127.0.0.1, server: localhost, request: "GET /log HTTP/1.1", host: "localhost"
            ```
            If invoked from within a plugin (for example, `key-auth`) it would include the
            namespace prefix:
            ``` plain
            2017/07/09 19:36:25 [error] 25932#0: *1 [kong] some_file.lua:54 [key-auth] hello world, client: 127.0.0.1, server: localhost, request: "GET /log HTTP/1.1", host: "localhost"
            ```

        Phases:
            init_worker, certificate, rewrite, access, header_filter, response, body_filter, log

        Example:
            kong.log.warn("something require attention")

            kong.log.err("something failed: ", err)

            kong.log.alert("something requires immediate action")

        :parameter *args: All params will be concatenated and stringified before being sent to the log.
        :type *args: Any

        :return: Throws an error on invalid inputs.

        :rtype: None
        """
        pass

    @staticmethod
    def info(*args: Any) -> None:
        """

            Similar to `kong.log()`, but the produced log has the severity given by
            `<level>`, instead of `notice`. The supported levels are:
            * `kong.log.alert()`
            * `kong.log.crit()`
            * `kong.log.err()`
            * `kong.log.warn()`
            * `kong.log.notice()`
            * `kong.log.info()`
            * `kong.log.debug()`
            Logs have the same format as that of `kong.log()`. For
            example, the following call:
            ``` lua
             kong.log.err("hello ", "world")
            ```
            would, within the core, produce a log line similar to:
            ``` plain
            2017/07/09 19:36:25 [error] 25932#0: *1 [kong] some_file.lua:54 hello world, client: 127.0.0.1, server: localhost, request: "GET /log HTTP/1.1", host: "localhost"
            ```
            If invoked from within a plugin (for example, `key-auth`) it would include the
            namespace prefix:
            ``` plain
            2017/07/09 19:36:25 [error] 25932#0: *1 [kong] some_file.lua:54 [key-auth] hello world, client: 127.0.0.1, server: localhost, request: "GET /log HTTP/1.1", host: "localhost"
            ```

        Phases:
            init_worker, certificate, rewrite, access, header_filter, response, body_filter, log

        Example:
            kong.log.warn("something require attention")

            kong.log.err("something failed: ", err)

            kong.log.alert("something requires immediate action")

        :parameter *args: All params will be concatenated and stringified before being sent to the log.
        :type *args: Any

        :return: Throws an error on invalid inputs.

        :rtype: None
        """
        pass

    @staticmethod
    def notice(*args: Any) -> None:
        """

            Similar to `kong.log()`, but the produced log has the severity given by
            `<level>`, instead of `notice`. The supported levels are:
            * `kong.log.alert()`
            * `kong.log.crit()`
            * `kong.log.err()`
            * `kong.log.warn()`
            * `kong.log.notice()`
            * `kong.log.info()`
            * `kong.log.debug()`
            Logs have the same format as that of `kong.log()`. For
            example, the following call:
            ``` lua
             kong.log.err("hello ", "world")
            ```
            would, within the core, produce a log line similar to:
            ``` plain
            2017/07/09 19:36:25 [error] 25932#0: *1 [kong] some_file.lua:54 hello world, client: 127.0.0.1, server: localhost, request: "GET /log HTTP/1.1", host: "localhost"
            ```
            If invoked from within a plugin (for example, `key-auth`) it would include the
            namespace prefix:
            ``` plain
            2017/07/09 19:36:25 [error] 25932#0: *1 [kong] some_file.lua:54 [key-auth] hello world, client: 127.0.0.1, server: localhost, request: "GET /log HTTP/1.1", host: "localhost"
            ```

        Phases:
            init_worker, certificate, rewrite, access, header_filter, response, body_filter, log

        Example:
            kong.log.warn("something require attention")

            kong.log.err("something failed: ", err)

            kong.log.alert("something requires immediate action")

        :parameter *args: All params will be concatenated and stringified before being sent to the log.
        :type *args: Any

        :return: Throws an error on invalid inputs.

        :rtype: None
        """
        pass

    @staticmethod
    def serialize() -> None:
        """

        """
        pass

    @staticmethod
    def set_serialize_value(key: str, value: Any, options: table) -> table:
        """

            Sets a value to be used on the `serialize` custom table.
            Logging plugins use the output of `kong.log.serialize()` as a base for their logs.
            This function lets you customize the log output.
            It can be used to replace existing values in the output, or to delete
            existing values by passing `nil`.
            **Note:** The type-checking of the `value` parameter can take some time, so
            it is deferred to the `serialize()` call, which happens in the log
            phase in most real-usage cases.

        Phases:
            certificate, rewrite, access, header_filter, response, body_filter, log

        Example:
            # Adds a new value to the serialized table

            kong.log.set_serialize_value("my_new_value", 1)

            assert(kong.log.serialize().my_new_value == 1)

            # Value can be a table

            kong.log.set_serialize_value("my", { new = { value = 2 } })

            assert(kong.log.serialize().my.new.value == 2)

            # It is possible to change an existing serialized value

            kong.log.set_serialize_value("my_new_value", 3)

            assert(kong.log.serialize().my_new_value == 3)

            # Unset an existing value by setting it to nil

            kong.log.set_serialize_value("my_new_value", nil)

            assert(kong.log.serialize().my_new_value == nil)

            # Dots in the key are interpreted as table accesses

            kong.log.set_serialize_value("my.new.value", 4)

            assert(kong.log.serialize().my.new_value == 4)

        :parameter key: The name of the field.
        :type key: str
        :parameter value: Value to be set. When a table is used, its keys must be numbers, strings, or booleans, and its values can be numbers, strings, or other tables like itself, recursively.
        :type value: Any
        :parameter options: Can contain two entries: options.mode can be `set` (the default, always sets), `add` (only add if entry does not already exist) and `replace` (only change value if it already exists).
        :type options: table

        :return: The request information table.

        :rtype: table
        """
        pass

    @staticmethod
    def warn(*args: Any) -> None:
        """

            Similar to `kong.log()`, but the produced log has the severity given by
            `<level>`, instead of `notice`. The supported levels are:
            * `kong.log.alert()`
            * `kong.log.crit()`
            * `kong.log.err()`
            * `kong.log.warn()`
            * `kong.log.notice()`
            * `kong.log.info()`
            * `kong.log.debug()`
            Logs have the same format as that of `kong.log()`. For
            example, the following call:
            ``` lua
             kong.log.err("hello ", "world")
            ```
            would, within the core, produce a log line similar to:
            ``` plain
            2017/07/09 19:36:25 [error] 25932#0: *1 [kong] some_file.lua:54 hello world, client: 127.0.0.1, server: localhost, request: "GET /log HTTP/1.1", host: "localhost"
            ```
            If invoked from within a plugin (for example, `key-auth`) it would include the
            namespace prefix:
            ``` plain
            2017/07/09 19:36:25 [error] 25932#0: *1 [kong] some_file.lua:54 [key-auth] hello world, client: 127.0.0.1, server: localhost, request: "GET /log HTTP/1.1", host: "localhost"
            ```

        Phases:
            init_worker, certificate, rewrite, access, header_filter, response, body_filter, log

        Example:
            kong.log.warn("something require attention")

            kong.log.err("something failed: ", err)

            kong.log.alert("something requires immediate action")

        :parameter *args: All params will be concatenated and stringified before being sent to the log.
        :type *args: Any

        :return: Throws an error on invalid inputs.

        :rtype: None
        """
        pass

    pass