# vim:fileencoding=utf-8:foldmethod=marker

# System {{{


from APP.config.log import LogProses, debugProses

from pathlib import Path
from fastapi import APIRouter, Request, Response, status
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.exceptions import HTTPException

from APP.config.dotenvfile import GetEnv

# from APP.config.util import Gen_Random_sha256, Gen_Random_string, Gen_Random_int

from APP.config.utility.randomGen import (
    Gen_Random_sha256,
    Gen_Random_int,
    Gen_Random_string,
    Gen_Random_UUID,
)

from APP.config.utility.util import Get_time_now


# INFO UPDATE PATH

# PATH_UPLOADFILE = Path(GetEnv("Folder.Upload.Path", "uploadFolder"))  # type: ignore
# PATH_TMP = Path("tmp")
# PATH_LOG = Path("log")


def redirect_url(url: str, statusCode=status.HTTP_301_MOVED_PERMANENTLY):
    return RedirectResponse(url, status_code=statusCode)


# }}}


# userCode {{{


# cache

from APP.config.manager import cachemanager

cache_manager = cachemanager.create()

# from APP.config.manager import filemanager

# globalFileProses = filemanager.create("tmp")


# DataBase Connections
from APP.config.manager.sqlmanager import SessionLocal, engine


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# }}}
