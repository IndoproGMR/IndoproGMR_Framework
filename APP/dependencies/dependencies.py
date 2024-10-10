# vim:fileencoding=utf-8:foldmethod=marker

# System {{{

from typing import Annotated
from fastapi import Header, HTTPException, Request

# from APP.config.cachemanager import cache_manager
# from APP.config.manager.cachemanager import cache_manager

from APP.config.manager import cachemanager

cache_manager = cachemanager.create()

# cache_manager = create_cache()


async def get_token_header(X_token: Annotated[str, Header()]):
    # return
    # return x_token
    if X_token == None:
        raise HTTPException(status_code=400, detail="No X-token cookie provided")

    if X_token != "fake_super_secret_token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    return X_token


async def get_query_token(token: str):
    return
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")


async def get_token_request(request: Request):
    token = request.cookies.get("X-token")

    if token == None:
        raise HTTPException(status_code=400, detail="No X-token cookie provided")

    if cache_manager.cache_get(token) == None:
        raise HTTPException(status_code=400, detail="No X-token cookie provided")

    return token


# }}}
