from time import sleep
from APP.config.View import view
from pydantic import BaseModel
from APP.routers.baseRouter import *
from APP.config.upload import saveFile
from typing import Annotated, Union
from helpers.testdemo import ohsit

from APP.dependencies.dependencies import get_token_header
from fastapi import UploadFile, File, Depends


router = APIRouter(
    prefix="/test",
    tags=["test"],
    responses={404: {"detail": "Not found"}},  # type: ignore
    # dependencies=[Depends(get_token_header)],
)


class Image(BaseModel):
    url: str
    name: str


@router.post("/uploadfile")
async def create_upload_file(detail_foto: str, file: UploadFile = File(...)):
    status, saved_filename = await saveFile(file, Path_FOLDER="pdf/now")
    if status:
        return ApiRespond(
            {"filename": saved_filename, "detail_foto": detail_foto},
            code=200,
            messages="berhasil",
        )
    else:
        return ApiRespond({"filename": saved_filename}, code=500, messages="gagal")


@router.post("/multiFiles")
async def method_Upload(
    files: Annotated[list[UploadFile], File()],
):
    for file in files:
        status, saved_filename = await saveFile(file, Path_FOLDER="pdf/now")
        if status is False:
            return {"detail": "Upload Failed"}

    return {"filename": "saved_filename"}


class TestModelNama(BaseModel):
    Nama: str


@router.post("/nama")
def method_name(
    NamaLengkap: TestModelNama,
    namaDepan: str,
    namaBelakang: str,
    namaTengah: Union[str, None] = None,
    image: Union[Image, None] = None,
):
    return {
        "respond": NamaLengkap,
        "namaDepan": namaDepan,
        "namaBelakang": namaBelakang,
        "namaTengah": namaTengah,
        "image": image,
    }


@router.get(
    "/",
    response_class=HTMLResponse,
)
def html(request: Request):
    data = [{"test": "isi data"}]
    return view(request, "test.html", data)


@router.get("/method_html", response_class=HTMLResponse)
async def method_html(request: Request):
    return view(request)


@router.get("/aaa/{id}")
async def root(id: str):
    # return {"message": "hello world", "id": id, "x_token": x_token}
    return {"message": "hello world", "id": id}


from APP.config.log import LogProses


@router.get("/api")
def read_root(request: Request):
    result = {
        "client_host": request.client.host,  # type: ignore
        "client_Port": request.client.port,  # type: ignore
        "request_url": request.url.path,
    }
    LogProses("read test api:" + request.client.host)  # type: ignore
    sleep(1)
    return ApiRespond(result)


@router.get("/request/{id}")
async def test(
    request: Request,
    id: str,
    namaDepan: str,
    namaBelakang: str,
    namaTengah: Union[str, None] = None,
):
    return {
        "id": id,
        "namaDepan": namaDepan,
        "namaBelakang": namaBelakang,
        "namaTengah": namaTengah,
        "request": request.url.components,
        "request4": request.cookies,
        "request5": request.client,
        "request6": request.headers,
        "request7": ohsit(),
    }


@router.get("/cache")
def cache():
    # cache_manager.cache_set("test1", ["test1", "test2", "test3"])
    # cache_manager.cache_set(
    # "test2", {"test1": "test2", "test3": ["test1", "test2", "test3"]}
    # )
    # return {"respond": cache_manager.cache_get("test2")}
    return {"respond": "asd"}


from APP.config.throttle import *


@router.get("/throttle")
@limiter.limit("10/minute")
async def throttle(request: Request):
    return {"message": "hello world"}


@router.get("/throttleclass")
@limiter.limit("10/minute")
async def throttleclass(request: Request):
    return {"msg": "Hello World"}


@router.get("/loadCache/{id}")
def LoadCache(request: Request, id: str):
    host = request.client.host  # type: ignore
    text = f"read test api: {host} id:{id}"

    array = ["a", "b", ["c1", "c2"], text]

    # cache_manager.cache_set(id, text, 10)
    # cache_manager.cache_set(f"array{id}", array)

    # sleep(10)

    dataCache = cache_manager.cache_get(id)
    dataCache2 = cache_manager.cache_get(f"array{id}")

    # cache_manager.cache_delete(id)

    return {"message": dataCache, "array": dataCache2}
