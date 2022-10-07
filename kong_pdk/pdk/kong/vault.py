# AUTO GENERATED BASED ON Kong 3.1.x, DO NOT EDIT
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

            Resolves the passed in reference and returns the value of it.

        Example:
            value, err = kong.vault.get("{vault://env/cert/key}")

        :parameter reference: reference to resolve
        :type reference: str

        :return: resolved value of the reference

        :rtype: str
        :return: error message on failure, otherwise `nil`

        :rtype: str
        """
        pass

    @staticmethod
    def is_reference(reference: str) -> bool:
        """

            Checks if the passed in reference looks like a reference.
            Valid references start with '{vault://' and end with '}'.
            If you need more thorough validation,
            use `kong.vault.parse_reference`.

        Example:
            kong.vault.is_reference("{vault://env/key}") # true

            kong.vault.is_reference("not a reference")   # false

        :parameter reference: reference to check
        :type reference: str

        :return: `true` is the passed in reference looks like a reference, otherwise `false`

        :rtype: bool
        """
        pass

    @staticmethod
    def parse_reference(reference: str) -> Tuple[table, str]:
        """

            Parses and decodes the passed in reference and returns a table
            containing its components.
            Given a following resource:
            ```lua
            "{vault://env/cert/key?prefix=SSL_#1}"
            ```
            This function will return following table:
            ```lua
            {
              name     = "env",  -- name of the Vault entity or Vault strategy
              resource = "cert", -- resource where secret is stored
              key      = "key",  -- key to lookup if the resource is secret object
              config   = {       -- if there are any config options specified
                prefix = "SSL_"
              },
              version  = 1       -- if the version is specified
            }
            ```

        Example:
            ref, err = kong.vault.parse_reference("{vault://env/cert/key?prefix=SSL_#1}") # table

        :parameter reference: reference to parse
        :type reference: str

        :return: a table containing each component of the reference, or `nil` on error

        :rtype: table
        :return: error message on failure, otherwise `nil`

        :rtype: str
        """
        pass

    pass