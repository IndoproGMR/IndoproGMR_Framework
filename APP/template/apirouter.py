from APP.routers.baseRouter import *

# from ..config.dependencies import *


router = APIRouter(
    prefix="/root",
    tags=["root"],
    responses={404: {"detail": "Not found"}},
    dependencies=[],
)


@router.get("/")
async def root():
    return {"message": "hello world"}
