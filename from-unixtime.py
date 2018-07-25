""" Convert unix time extension """

import datetime
from albertv0 import *

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Convert unixtime to date"
__version__ = "1.3"
__trigger__ = "ut "
__author__ = "Eduard Gert"
__dependencies__ = []

iconPath = iconLookup('process-stop')


def handleQuery(query):
    if query.isTriggered:
        s = query.string.strip()
        if len(s) == 10:
            result = datetime.datetime.fromtimestamp(int(s)).strftime('%Y-%m-%d %H:%M:%S')
        elif len(s) == 13:
            result = datetime.datetime.fromtimestamp(int(s[:-3])).strftime('%Y-%m-%d %H:%M:%S')

        item = Item(
            id="trash-open",
            icon=iconPath,
            text=result,
            subtext="Convert unixtime to date",
            completion="trash"
        )

        item.addAction(ClipAction("Copy result to clipboard", result))

        return item