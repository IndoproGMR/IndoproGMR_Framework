import json
import redis
from APP.config.dotenvfile import getenvval
from .converter_Cache import convert_from_cache, convert_to_cache


class RedisCache:
    def __init__(self):
        self.r = redis.Redis(
            host=getenvval("cache.host"),  # type: ignore
            port=getenvval("cache.port"),  # type: ignore
            db=getenvval("cache.database"),  # type: ignore
            password=getenvval("cache.password"),
        )

    def cache_get(self, key):
        result = self.r.get(key)
        if result is not None:
            result = result.decode("utf-8")  # type: ignore
            result = convert_from_cache(result)
        return result

    def cache_set(self, key, value, ttl=None):
        converted_value = convert_to_cache(value)
        self.r.set(key, converted_value, ex=ttl)

    def cache_delete(self, key):
        self.r.delete(key)
