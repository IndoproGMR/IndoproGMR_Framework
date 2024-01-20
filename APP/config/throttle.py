from slowapi.util import get_remote_address
from slowapi import Limiter
from APP.config.dotenvfile import getenvval

redis_uri = "redis://" + getenvval("cache.host", "localhost") + ":" + getenvval(
    "cache.port", "6379")+"/"+getenvval("cache.database", "0")


if getenvval("cache.type", "file") == "redis":
    limiter = Limiter(key_func=get_remote_address, default_limits=[
        "60/minute"], storage_uri=redis_uri)
else:
    limiter = Limiter(key_func=get_remote_address, default_limits=[
        "60/minute"])

# !add to main.py
# from slowapi.errors import RateLimitExceeded
# from slowapi import Limiter, _rate_limit_exceeded_handler
# limiter = Limiter(key_func=get_remote_address)
# app.state.limiter = limiter
# app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# !add to main.py for global limit
# from slowapi import Limiter, _rate_limit_exceeded_handler
# from slowapi.util import get_remote_address
# from slowapi.middleware import SlowAPIMiddleware
# from slowapi.errors import RateLimitExceeded
# limiter = Limiter(key_func=get_remote_address, default_limits=["1/minute"])
# app.state.limiter = limiter
# app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
# app.add_middleware(SlowAPIMiddleware)
