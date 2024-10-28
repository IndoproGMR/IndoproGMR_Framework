from time import sleep

from .baseRouter import *

router = APIRouter(
    prefix="/cache",
    tags=["democache"],
)


@router.get("/createDataCache")
async def createDataCache():
    data = Gen_Random_sha256()
    cache_manager.add("sha256", data, 30)
    sleep(2)
    return {"message": data}


@router.get("/getDataCache")
def getDataCache():
    data = cache_manager.get("sha256")
    if data is None:
        data = "kosong"
    return {"message": data}


@router.get("/setObj")
def method_name():
    data = Gen_Random_sha256()
    dataObj = {"aaaa": data}
    cache_manager.add("sha256", dataObj, 30)
    return {"message": dataObj}
