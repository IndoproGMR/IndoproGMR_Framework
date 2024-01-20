from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from APP.config.ResponseStandardization import *
from pathlib import Path
from APP.config.dotenvfile import getenvval
from APP.config.throttle import *
# from APP.config.View import view


PATH_UPLOADFILE = Path(getenvval("Folder.Upload.Path",
                                 "uploadFolder"))  # type: ignore
PATH_TMP = Path("tmp")


def redirect_url(url: str):
    return RedirectResponse(url, status_code=303)
