from pathlib import Path
from fastapi import APIRouter, Request, Response
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from APP.config.ResponseStandardization import (
    ApiRespond,
    ApiRespond_notFound,
    ApiRespond_unauthorized,
)
from APP.config.dotenvfile import getenvval
from APP.config.util import Gen_Random_sha256, Gen_Random_string, Gen_Random_int

from APP.config.cachemanager import cache_manager

# cache_manager = create_cache()

PATH_UPLOADFILE = Path(getenvval("Folder.Upload.Path", "uploadFolder"))  # type: ignore
PATH_TMP = Path("tmp")
PATH_LOG = Path("log")


def redirect_url(url: str):
    return RedirectResponse(url, status_code=303)
