# AUTO GENERATED BASED ON Kong 2.3.x, DO NOT EDIT
# Original source path: kong/pdk.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str

from .kong.client import client as cls_client
from .kong.cluster import cluster as cls_cluster
from .kong.ctx import ctx as cls_ctx
from .kong.ip import ip as cls_ip
from .kong.log import log as cls_log
from .kong.nginx import nginx as cls_nginx
from .kong.node import node as cls_node
from .kong.request import request as cls_request
from .kong.response import response as cls_response
from .kong.router import router as cls_router
from .kong.service import service as cls_service
from .kong.table import table as cls_table

class kong():

    client = cls_client
    cluster = cls_cluster
    ctx = cls_ctx
    ip = cls_ip
    log = cls_log
    nginx = cls_nginx
    node = cls_node
    request = cls_request
    response = cls_response
    router = cls_router
    service = cls_service
    table = cls_table

    pass