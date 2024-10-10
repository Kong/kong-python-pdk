# AUTO GENERATED BASED ON Kong 3.8.x, DO NOT EDIT
# Original source path: kong/pdk/telemetry.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str


class telemetry():


    @staticmethod
    def log(plugin_name: str, plugin_config: table, message_type: str, message: str, attributes: table) -> None:
        """

            Records a structured log entry, to be reported via the OpenTelemetry plugin.
            This function has a dependency on the OpenTelemetry plugin, which must be
            configured to report OpenTelemetry logs.

        Phases:
            rewrite, access, balancer, timer, header_filter, response, body_filter, log

        Example:
            attributes = {

            http_method = kong.request.get_method()

            ["node.id"] = kong.node.get_id(),

            hostname = kong.node.get_hostname(),

            }

            ok, err = kong.telemetry.log("my_plugin", conf, "result", "successful operation", attributes)

        :parameter plugin_name: the name of the plugin
        :type plugin_name: str
        :parameter plugin_config: the plugin configuration
        :type plugin_config: table
        :parameter message_type: the type of the log message, useful to categorize
            the log entry
        :type message_type: str
        :parameter message: the log message
        :type message: str
        :parameter attributes: structured information to be included in the
            `attributes` field of the log entry
        :type attributes: table

        """
        pass

    pass
