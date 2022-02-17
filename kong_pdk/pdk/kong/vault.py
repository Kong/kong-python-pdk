# AUTO GENERATED BASED ON Kong 2.7.x, DO NOT EDIT
# Original source path: kong/pdk/vault.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str


class vault():


    @staticmethod
    def get(reference: str) -> Tuple[str, str]:
        """
        local value, err = kong.vault.get("{vault://env/cert/key}")
        :param reference: reference to resolve
        :returns resolved value of the reference
        returns error message on failure, otherwise `nil`
        """
        pass

    @staticmethod
    def is_reference(reference: str) -> bool:
        """
        kong.vault.is_reference("{vault://env/key}") -- true
        kong.vault.is_reference("not a reference")   -- false
        :param reference: reference to check
        :returns `true` is the passed in reference looks like a reference, otherwise `false`
        """
        pass

    @staticmethod
    def parse_reference(reference: str) -> Tuple[table, str]:
        """
        local ref, err = kong.vault.parse_reference("{vault://env/cert/key?prefix=SSL_#1}") -- table
        :param reference: reference to parse
        :returns a table containing each component of the reference, or `nil` on error
        returns error message on failure, otherwise `nil`
        """
        pass

    pass