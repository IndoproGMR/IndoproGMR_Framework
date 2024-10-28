# vim:fileencoding=utf-8:foldmethod=marker

# System {{{

from .baseRouter import *
from typing import Annotated
from fastapi import Depends, Form
from pydantic import BaseModel


# !set dependencies global
# ?from APP.dependencies.dependencies import get_token_request
router = APIRouter(
    prefix="/demo",
    tags=["demo"],
    # ?dependencies=[Depends(get_token_request)],
)


@router.get("/DemoGet")
def DemoGet():
    return {"message": "hello world"}


@router.get("/DemoGetQuery")
def DemoGetQuery(id: int):
    return {"id": id}


@router.post("/DemoForm")
def DemoForm(
    DemoString: Annotated[str, Form()],
    Demoint: Annotated[int, Form()],
    Toggle: bool = Form(False),
    ToggleTrue: bool = Form(True),
):
    return {
        "DemoString": DemoString,
        "Demoint": Demoint,
        "Toggle": Toggle,
        "ToggleTrue": ToggleTrue,
    }


class DemoModel(BaseModel):
    DemoString: Annotated[str, Form()]
    Demoint: Annotated[int, Form()]
    Toggle: bool = Form(False)
    ToggleTrue: bool = Form(True)


@router.post("/DemoBaseModel")
def DemoBaseModel(data: DemoModel):
    return {
        "DemoString": data.DemoString,
        "Demoint": data.Demoint,
        "Toggle": data.Toggle,
        "ToggleTrue": data.ToggleTrue,
    }


@router.get("/DemoRedirectURL")
def DemoRedirectURL():
    return redirect_url("/")


@router.post("/DemoSetCookieNRedirectURL")
def DemoSetCookieNRedirectURL(data: DemoModel):
    response = redirect_url("/")
    response.set_cookie(key="X-token", value="fake_super_secret_token")

    return response


# !set dependencies to single route
from APP.dependencies.dependencies import get_token_request


@router.get("/DemoDepency", dependencies=[Depends(get_token_request)])
def DemoDepency():
    return {"message": "hello world"}


# !import view first
from APP.config.View import view


@router.get("/DemoView", response_class=HTMLResponse)
async def DemoView(request: Request):
    return view(request, "index.html")


# !import file first
from APP.config.upload import saveFile
from fastapi import UploadFile, File


@router.post("/uploadfile")
async def DemoUploadFile(detail_foto: str, file: UploadFile = File(...)):
    status, saved_filename = await saveFile(file, Path_FOLDER="File")

    if status:
        return {"filename": saved_filename, "detail_foto": detail_foto}
    else:
        return {"filename": saved_filename}


# !import throttle first
from APP.config.throttle import *


@router.get("/throttle")
@limiter.limit("10/minute")
async def throttle(request: Request):
    return {"message": "hello world"}


# }}}
