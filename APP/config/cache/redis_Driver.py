# vim:fileencoding=utf-8:foldmethod=marker

# System {{{

# redis cache Driver
import redis

from .converter_Cache import convert_from_cache, convert_to_cache
from APP.config.log import LogProses
from APP.config.dotenvfile import GetEnv


class RedisCache:
    def __init__(self):
        try:
            if GetEnv("Plugin_Docker", "False").str() != "True":
                self.r = redis.Redis(
                    host=GetEnv("cache_host", "127.0.0.1").str(),
                    port=GetEnv("cache_port", 6379).int(),
                    db=GetEnv("cache_database", 0).int(),
                    password=GetEnv("cache_password", "").str(),
                )
            else:
                self.r = redis.Redis(host="redis", port=6380, db=0)
        except Exception as e:
            LogProses(f"Error during Redis Cache Init: {e}")

    def get(self, key):
        if GetEnv("cache_bypass", "False").str() == "True":
            return None

        if key is None:
            return None

        try:
            result = self.r.get(key)
        except Exception as e:
            LogProses(f"Error getting Cache: {e}")
            return None

        if result is not None:
            result = result.decode("utf-8")  # type: ignore
            result = convert_from_cache(result)
        return result

    def add(self, key, value, ttl=None):
        try:
            self.r.set(key, convert_to_cache(value), ex=ttl)
            return True
        except Exception as e:
            LogProses(f"Error saving cache: {e}")
            return False

    def delete(self, key):
        try:
            self.r.delete(key)
            return True
        except Exception as e:
            LogProses(f"Error deleting cache: {e}")
            return False


# }}}
