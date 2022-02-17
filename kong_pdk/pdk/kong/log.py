# AUTO GENERATED BASED ON Kong 2.7.x, DO NOT EDIT
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
        kong.log.warn("something require attention")
        kong.log.err("something failed: ", err)
        kong.log.alert("something requires immediate action")
        :param *args: All params will be concatenated and stringified before being sent to the log.
        :returns Throws an error on invalid inputs.
        """
        pass

    @staticmethod
    def crit(*args: Any) -> None:
        """
        kong.log.warn("something require attention")
        kong.log.err("something failed: ", err)
        kong.log.alert("something requires immediate action")
        :param *args: All params will be concatenated and stringified before being sent to the log.
        :returns Throws an error on invalid inputs.
        """
        pass

    @staticmethod
    def debug(*args: Any) -> None:
        """
        kong.log.warn("something require attention")
        kong.log.err("something failed: ", err)
        kong.log.alert("something requires immediate action")
        :param *args: All params will be concatenated and stringified before being sent to the log.
        :returns Throws an error on invalid inputs.
        """
        pass

    @staticmethod
    def deprecation(*args: Any) -> None:
        """
        kong.log.deprecation("hello ", "world")
        kong.log.deprecation("hello ", "world", { after = "2.5.0" })
        kong.log.deprecation("hello ", "world", { removal = "3.0.0" })
        kong.log.deprecation("hello ", "world", { after = "2.5.0", removal = "3.0.0" })
        kong.log.deprecation("hello ", "world", { trace = true })
        :param *args: all params will be concatenated and stringified before being sent to the log
        (if the last param is a table, it is considered as a deprecation metadata)
        :returns throws an error on invalid inputs.
        """
        pass

    @staticmethod
    def err(*args: Any) -> None:
        """
        kong.log.warn("something require attention")
        kong.log.err("something failed: ", err)
        kong.log.alert("something requires immediate action")
        :param *args: All params will be concatenated and stringified before being sent to the log.
        :returns Throws an error on invalid inputs.
        """
        pass

    @staticmethod
    def info(*args: Any) -> None:
        """
        kong.log.warn("something require attention")
        kong.log.err("something failed: ", err)
        kong.log.alert("something requires immediate action")
        :param *args: All params will be concatenated and stringified before being sent to the log.
        :returns Throws an error on invalid inputs.
        """
        pass

    @staticmethod
    def notice(*args: Any) -> None:
        """
        kong.log.warn("something require attention")
        kong.log.err("something failed: ", err)
        kong.log.alert("something requires immediate action")
        :param *args: All params will be concatenated and stringified before being sent to the log.
        :returns Throws an error on invalid inputs.
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
        -- Adds a new value to the serialized table
        kong.log.set_serialize_value("my_new_value", 1)
        assert(kong.log.serialize().my_new_value == 1)
        -- Value can be a table
        kong.log.set_serialize_value("my", { new = { value = 2 } })
        assert(kong.log.serialize().my.new.value == 2)
        -- It is possible to change an existing serialized value
        kong.log.set_serialize_value("my_new_value", 3)
        assert(kong.log.serialize().my_new_value == 3)
        -- Unset an existing value by setting it to nil
        kong.log.set_serialize_value("my_new_value", nil)
        assert(kong.log.serialize().my_new_value == nil)
        -- Dots in the key are interpreted as table accesses
        kong.log.set_serialize_value("my.new.value", 4)
        assert(kong.log.serialize().my.new_value == 4)
        :param key: The name of the field.
        :param value: Value to be set. When a table is used, its keys must be numbers, strings, or booleans, and its values can be numbers, strings, or other tables like itself, recursively.
        :param options: Can contain two entries: options.mode can be `set` (the default, always sets), `add` (only add if entry does not already exist) and `replace` (only change value if it already exists).
        :returns The request information table.
        """
        pass

    @staticmethod
    def warn(*args: Any) -> None:
        """
        kong.log.warn("something require attention")
        kong.log.err("something failed: ", err)
        kong.log.alert("something requires immediate action")
        :param *args: All params will be concatenated and stringified before being sent to the log.
        :returns Throws an error on invalid inputs.
        """
        pass

    pass