# AUTO GENERATED BASED ON Kong 3.1.x, DO NOT EDIT
# Original source path: kong/pdk.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str

from .client import client as cls_client
from .cluster import cluster as cls_cluster
from .ctx import ctx as cls_ctx
from .ip import ip as cls_ip
from .log import log as cls_log
from .nginx import nginx as cls_nginx
from .node import node as cls_node
from .request import request as cls_request
from .response import response as cls_response
from .router import router as cls_router
from .service import service as cls_service
from .vault import vault as cls_vault

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
    vault = cls_vault

    pass