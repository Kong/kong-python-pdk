# coding:utf-8
# constants module
# Contributor:
#      fffonion        <fffonion@gmail.com>

import os
import sys
import locale

PY3K = sys.version_info.major == 3
IRONPYTHON = sys.platform == 'cli'
EXEBUNDLE = getattr(sys, 'frozen', False)
LOCALE = locale.getdefaultlocale()[0]
CODEPAGE = locale.getdefaultlocale()[1] or 'ascii'

__version__ = 0.32

# https://github.com/soimort/you-get/you-get
if getattr(sys, 'frozen', False):
    # The application is frozen
    FILEPATH = os.path.dirname(os.path.realpath(sys.executable))
else:
    # The application is not frozen
    # Change this bit to match where you store your data files:
    FILEPATH = sys.path[0]
