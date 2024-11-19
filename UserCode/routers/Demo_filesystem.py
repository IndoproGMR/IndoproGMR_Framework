from fastapi import UploadFile
from APP.config.manager import filemanager
from .baseRouter import *

# from APP.config.utility.simulasi import start_heavy_process, start_async_heavy_process

router = APIRouter(
    prefix="/filesystem",
    tags=["demoFilesystem"],
)

fileproses = filemanager.create("tmp/demo")


@router.get("/createFolder/{test}")
async def createFolder(test: str):
    # print(f"start saving file: {test}")
    # background_tasks.add_task(start_heavy_process)
    # background_tasks.add_task(start_async_heavy_process)

    await fileproses.SaveFolder(f"test/createFolder/{test}")
    # print(f"saving file done: {test}")
    return {"message": "hello world"}


@router.get("/deleteFolder")
async def deleteFolder():
    await fileproses.DeleteFolder("test")
    return {"message": "hello world"}


@router.get("/deleteFolder/rec")
async def deleteFolderRec():
    await fileproses.DeleteFolder("test", recursive=True)
    return {"message": "hello world"}


@router.get("/deleteFolder/withcontent")
async def deleteFoldercon():
    await fileproses.DeleteFolder("test", deleteWithContent=True)
    return {"message": "hello world"}


@router.get("/createFile")
async def createFile():
    data = f"isi file: {Get_time_now()}"

    await fileproses.SaveFile(data, "testcreate.txt", "test")
    return {"message": "hello world"}


@router.get("/readFile")
async def readFile():
    data = await fileproses.ReadFile("testcreate.txt", "test")
    print(data)
    return {"message": "hello world"}


@router.get("/deleteFile")
async def deleteFile():
    await fileproses.DeleteFile("testcreate.txt", "test")
    return {"message": "hello world"}


@router.post("/uploadFile")
async def uploadFile(file: UploadFile):
    # print(file.filename)
    print(file.content_type)

    await fileproses.SaveFile(
        file, file.filename, filter_types=["image/png", "text/x-log"]
    )
    return {"message": "hello world"}


@router.get("/readImage")
async def readImage():
    return await fileproses.ReadFile("Belakang.png", file_mode="rb")
    return {"message": "hello world"}


# @router.post("/")
# async def method_Upload(file: UploadFile):
# status, saved_filename = await saveFile(file)
# if status:
# return {"filename": saved_filename}
# else:
# return {"detail":"Upload Failed"}
