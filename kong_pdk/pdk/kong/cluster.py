# AUTO GENERATED BASED ON Kong 3.1.x, DO NOT EDIT
# Original source path: kong/pdk/cluster.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str


class cluster():


    @staticmethod
    def get_id() -> Tuple[str, str]:
        """

            Returns the unique ID for this Kong cluster. If Kong
            is running in DB-less mode without a cluster ID explicitly defined,
            then this method returns `nil`.
            For hybrid mode, all control planes and data planes belonging to the same
            cluster return the same cluster ID. For traditional database-based
            deployments, all Kong nodes pointing to the same database also return
            the same cluster ID.

        Example:
            id, err = kong.cluster.get_id()

            if err:

                # handle errorif not id:

                # no cluster ID is available# use id here

        :return: The v4 UUID used by this cluster as its ID.

        :rtype: str
        :return: An error message.

        :rtype: str
        """
        pass

    pass