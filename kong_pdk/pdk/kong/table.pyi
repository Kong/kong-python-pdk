# AUTO GENERATED BASED ON Kong 2.3.x, DO NOT EDIT
# Original source path: kong/pdk/table.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str

from .table.clear import clear as cls_clear
from .table.new import new as cls_new

class table():

    clear = cls_clear
    new = cls_new

    pass