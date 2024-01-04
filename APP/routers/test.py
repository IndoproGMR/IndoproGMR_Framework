import pprint
from APP.config import upload
from APP.routers.baseRouter import *
from pydantic import BaseModel
from typing import Union

from helpers.testdemo import ohsit

from APP.config.cachemanager import create_cache

from APP.config.upload import *

cache_manager = create_cache()


class TestModelNama(BaseModel):
    Nama: str


class Image(BaseModel):
    url: str
    name: str


router = APIRouter(
    prefix="/test",
    tags=["test"],
    responses={404: {"detail": "Not found"}},
)


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


@router.get("/", response_class=HTMLResponse)
def html(request: Request):
    data = [{"test": "isi data"}]
    return view(request, "views/test.html", data)


@router.get("/aaa/{id}")
async def root(id: str):
    return {"message": "hello world", "id": id}


@router.get("/api")
def read_root(request: Request):
    result = {
        "client_host": request.client.host,  # type: ignore
        "client_Port": request.client.port,  # type: ignore
        "request_url": request.url.path,
    }
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

    # data = {"a": "test1", "b": "test2", "c": "test3"}

    # data = "aaaaaaaaaaa"

    # cache_manager.cache_set("test", data)
    # result = cache_manager.cache_get("test")
    # return result

    # result_json = cache_manager.cache_get("test")

    # if result_json is not None:
    #     result = json.loads(result_json)
    #     return result
    # else:
    #     return None

    # Cacheset(key="test", value=data)
    # Cacheset("test", "test")
    # return Cacheget("test")
    # if Cacheget("test") == "test":
    # return "True"
    # else:
    # return "False"
    # return


# return Occupation.CountOccupation()


@router.get("/cache")
def cache():
    # if cache_manager.cache_get("test"):
    cache_manager.cache_set("test", ["test1", "test2", "test3"])

    return {"respond": cache_manager.cache_get("test")}
    # return {"message": "hello world"}


class FileValidasi(BaseModel):
    upload_file: UploadFile


@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    if saveFile(file):
        return JSONResponse(content={"filename": file.filename}, status_code=200)
    else:
        return JSONResponse(content={"detail": "gagal"}, status_code=500)
