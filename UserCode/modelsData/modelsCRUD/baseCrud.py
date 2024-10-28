# vim:fileencoding=utf-8:foldmethod=marker

# System {{{

from sqlalchemy.orm import Session

# from APP.models.modelsTable import Demo as mTDemo
# from APP.models.modelsSchemas import Demo as mSDemo


import time
from datetime import datetime


def getUnixTimeStamp():
    # return time.time() + 25200  # tambahan 7 jam untuk timezone asia/Jakarta
    # time.
    return time.time()


def getHumanTime():
    return datetime.utcfromtimestamp(getUnixTimeStamp()).strftime("%Y-%m-%d %H:%M:%S")


# }}}
