from .baseRouter import *

# import view lib
from APP.config.view import view

router = APIRouter(
    prefix="/view",
    tags=["demoView"],
)


@router.get("/First", response_class=HTMLResponse)
async def method_html(request: Request):
    data = {"RanCode": Gen_Random_sha256()}
    return view(request, "index.html", data)


@router.get("/UploadFile", response_class=HTMLResponse)
async def UploadFile(request: Request):
    return view(request, "UploadFile.html")
