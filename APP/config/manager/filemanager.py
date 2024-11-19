# vim:fileencoding=utf-8:foldmethod=marker


from APP.config.dotenvfile import GetEnv
from APP.config.filesave.local_Driver import local_Driver
from APP.config.log import LogProses, debugProses


def create(prefix_path: str):
    # LogProses("[WIP] Menggunakan {file_Driver} Driver", forcePrint=True)
    # debugProses("[WIP] Menggunakan {file_Driver} Driver")
    return local_Driver(prefix_path)
