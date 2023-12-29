import json
from APP.config.dotenvfile import getenvval
import redis


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
            result = self._convert_from_cache(result)
        return result

    def cache_set(self, key, value, ttl=None):
        converted_value = self._convert_to_cache(value)
        self.r.set(key, converted_value, ex=ttl)

    def cache_delete(self, key):
        self.r.delete(key)

    def _convert_to_cache(self, value):
        # Mengonversi nilai ke dalam bentuk yang sesuai untuk disimpan di cache
        return json.dumps(value)

    def _convert_from_cache(self, value):
        # Mengonversi nilai dari bentuk yang disimpan di cache ke bentuk semula
        return json.loads(value)
