# vim:fileencoding=utf-8:foldmethod=marker

# System {{{

from slowapi.util import get_remote_address
from slowapi import Limiter
from APP.config.dotenvfile import GetEnv


redis_uri = GetEnv("cache_redis_uri").str()
default_global_limit = GetEnv("cache_global_limit", "60/minute").str()


if GetEnv("cache_redis_uri", "None") == "None":
    host = GetEnv("cache_host", "localhost").str()
    port = GetEnv("cache_port", 6379).str()

    username = GetEnv("cache_username", "None").str()
    password = GetEnv("cache_password", "None").str()
    db = GetEnv("cache_database", "0").str()

    if GetEnv("Plugin_Docker", "False").str() != "True":
        port = "6380"
        host = "redis"

    if GetEnv("cache_username", "").str() != "":
        redis_uri = f"redis://{username}:{password}@{host}:{port}/{db}"

        # redis_uri = (
        #     "redis://"
        #     + GetEnv("cache_username", "None").str()
        #     + ":"
        #     + GetEnv("cache_password", "None").str()
        #     + "@"
        #     + GetEnv("cache_host", "localhost").str()
        #     + ":"
        #     + GetEnv("cache_port", "6379").str()
        #     + "/"
        #     + GetEnv("cache_database", "0").str()
        # )
    else:
        redis_uri = f"redis://{host}:{port}/{db}"
        # redis_uri = (
        #     "redis://"
        #     + GetEnv("cache_host", "localhost").str()
        #     + ":"
        #     + GetEnv("cache_port", "6379").str()
        #     + "/"
        #     + GetEnv("cache_database", "0").str()
        # )

print(redis_uri)

if GetEnv("cache_type", "file") == "redis":
    limiter = Limiter(
        key_func=get_remote_address,
        default_limits=[default_global_limit],
        storage_uri=redis_uri,
    )
else:
    limiter = Limiter(
        key_func=get_remote_address, default_limits=[default_global_limit]
    )

# INFO add to main.py
# from slowapi.errors import RateLimitExceeded
# from slowapi import Limiter, _rate_limit_exceeded_handler
# limiter = Limiter(key_func=get_remote_address)
# app.state.limiter = limiter
# app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# INFO add to main.py for global limit
# from slowapi import Limiter, _rate_limit_exceeded_handler
# from slowapi.util import get_remote_address
# from slowapi.middleware import SlowAPIMiddleware
# from slowapi.errors import RateLimitExceeded
# limiter = Limiter(key_func=get_remote_address, default_limits=["1/minute"])
# app.state.limiter = limiter
# app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
# app.add_middleware(SlowAPIMiddleware)

# }}}
