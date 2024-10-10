# vim:fileencoding=utf-8:foldmethod=marker

# System {{{


from APP.config.log import LogProses

from pathlib import Path
from fastapi import APIRouter, Request, Response, status
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.exceptions import HTTPException

from APP.config.dotenvfile import GetEnv
from APP.config.util import Gen_Random_sha256, Gen_Random_string, Gen_Random_int


# INFO UPDATE PATH

# PATH_UPLOADFILE = Path(GetEnv("Folder.Upload.Path", "uploadFolder"))  # type: ignore
# PATH_TMP = Path("tmp")
# PATH_LOG = Path("log")


def redirect_url(url: str):
    return RedirectResponse(url, status_code=status.HTTP_303_SEE_OTHER)


# }}}


# userCode {{{


# cache

from APP.config.manager import cachemanager

cache_manager = cachemanager.create()

from APP.config.manager import filemanager

fileproses = filemanager.create("")


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
