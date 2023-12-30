from APP.routers.baseRouter import *
from APP.models import Occupation
from APP.config.cachemanager import create_cache

cache_manager = create_cache()

router = APIRouter(
    prefix="/test",
    tags=["test"],
    responses={404: {"detail": "Not found"}},
    dependencies=[],
)


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


@router.get("/oc")
async def test():
    # data = {"a": "test1", "b": "test2", "c": "test3"}

    # data = "aaaaaaaaaaa"

    # cache_manager.cache_set("test", data)
    result = cache_manager.cache_get("test")
    return result

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
