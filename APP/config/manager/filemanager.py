# vim:fileencoding=utf-8:foldmethod=marker

# System {{{


from APP.config.dotenvfile import GetEnv
from APP.config.filesave.local_Driver import local_Driver
from APP.config.log import LogProses


def create(prefix_path: str):
    LogProses("[WIP] Menggunakan {file_Driver} Driver", forcePrint=True)
    # print("membuat sistem FileProses")
    return local_Driver(prefix_path)


# }}}
