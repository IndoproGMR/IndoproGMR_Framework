# redis cache Driver
import redis
from APP.config.dotenvfile import getenvval
from .converter_Cache import convert_from_cache, convert_to_cache
from APP.config.log import LogProses


class RedisCache:
    def __init__(self):
        try:
            self.r = redis.Redis(
                host=getenvval("cache.host", "localhosth"),  # type: ignore
                port=getenvval("cache.port", 6379),  # type: ignore
                db=getenvval("cache.database", 0),  # type: ignore
                password=getenvval("cache.password", ""),
            )
            LogProses("Success connetion to redis")
        except Exception as e:
            # print(f"Error during Redis Cache Init: {e}")
            LogProses(f"Error during Redis Cache Init: {e}")

    def cache_get(self, key):
        if key is None:
            return None

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
