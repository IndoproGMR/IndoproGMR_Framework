from typing import Union

from APP.config.dotenvfile import getenvval
from APP.config.cache.file import FileCache
from APP.config.cache.redis import RedisCache


def create_cache(cache_file_path: Union[str, None] = "tmp/cache/"):
    cache_type = getenvval("cache.type", "file")

    if cache_type is None:
        cache_type = "file"

    if cache_type == "redis":
        return RedisCache()
    elif cache_type == "file":
        return FileCache(cache_file_path, "cache.json")
    else:
        raise ValueError(f"Invalid cache type: {cache_type}")


def cache_get(self, key):
    return self.cache.cache_get(key)


def cache_set(self, key, value, ttl=None):
    self.cache.cache_set(key, value, ttl)


def cache_delete(self, key):
    self.cache.cache_delete(key)
