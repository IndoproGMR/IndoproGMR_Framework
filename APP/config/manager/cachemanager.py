# vim:fileencoding=utf-8:foldmethod=marker

# System {{{

from typing import Union

from APP.config.dotenvfile import GetEnv

from APP.config.log import LogProses

# Cache Driver
from APP.config.cache.file_Driver import FileCache
from APP.config.cache.redis_Driver import RedisCache

# from APP.config.cache.kv_Driver import


def create():
    cache_type = GetEnv("cache_type", "file").str()
    LogProses(f"Menggunakan {cache_type} Driver", forcePrint=True)

    if cache_type is None:
        cache_type = "file"

    if cache_type == "redis":
        return RedisCache()

    elif cache_type == "file":
        return FileCache()

    else:
        # raise ValueError(f"Invalid cache type: {cache_type}")
        raise LogProses(f"Invalid cache type: {cache_type}")


# }}}
