from APP.routers.baseRouter import *
from APP.model import Occupation


router = APIRouter(
    prefix="/test",
    tags=["test"],
    responses={404: {"detail": "Not found"}},
    dependencies=[],
)


@router.get("/", response_class=HTMLResponse)
def html(request: Request):
    data = [{"test": "isi data"}]
    return view(request, "view/test.html", data)


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
    return Occupation.CountOccupation()
