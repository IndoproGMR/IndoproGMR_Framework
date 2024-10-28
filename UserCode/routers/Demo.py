from datetime import datetime
import io
import json
from fastapi.responses import StreamingResponse
from sqlalchemy import true


from .baseRouter import *
from apscheduler.schedulers.background import BackgroundScheduler

schedulers = BackgroundScheduler()

router = APIRouter(
    # prefix="/",
    tags=["demo"],
)


@router.get("/asd")
def aaaaaa():
    LogProses("aaaaaa")

    # fileproses.SaveFile()
    return {"message": "hello world"}


@router.get("/cronJob")
def method_name():
    data = schedulers.print_jobs()
    print(data)
    return {"message": "hello world"}


@router.get("/buatfolder")
async def membuatFolder():
    await fileproses.SaveFolder("tmp/aa/1/2/3/4/5")
    return {"message": "hello world"}


@router.get("/buatfile")
async def membuatFile():
    filecontent = """aaaaaaaaaaaaaaaaaa
ini line 2
3"""

    datajson = {"data": "aaaa", "data2": ["bbb", "ccc"]}

    await fileproses.SaveFile(json.dumps(datajson), "datajsonAsli.json", "tmp")

    # await fileproses.SaveFile(filecontent, "filesave.txt", "tmp")

    # await fileproses.SaveFile(filecontent, "filesave.txt", "tmp", {"txt": "txt/plain"})

    # await fileproses.SaveFile(filecontent, "filesave.txt", "tmp/aa/1/2/3")
    # await fileproses.SaveFile(filecontent, "filesave.txt", "tmp")
    return {"message": "hello world"}


@router.get("/readFile")
async def readFile():
    # data = await fileproses.ReadFile("datajsonAsli.json", "tmp")

    # return {"message": data}

    data = await fileproses.ReadFile("1530851043656.jpg", "tmp", file_mode="rb")

    # data = await fileproses.ReadFile("testImage.png", "tmp", file_mode="rb")

    # data = await fileproses.ReadFile("testpdf.pdf", "tmp", file_mode="rb")

    return data


@router.get("/hapusFile")
async def hapusFile():
    await fileproses.DeleteFile("filesave.txt", "tmp/aa/1/2/3")
    return {"message": "hello world"}


@router.get("/hapusFolder")
async def hapusFolder():
    await fileproses.DeleteFolder("tmp/*", deleteWithContent=True)
    # await fileproses.DeleteFolder("tmp/aa/1/2", recursive=True)

    return {"message": "hello world"}


from fastapi import UploadFile

# from APP.config.upload import saveFile


@router.post("/UploadFile")
async def method_Upload(filedata: UploadFile):

    print(
        f"""Data File Upload
nama File: {filedata.filename}
file type: {filedata.content_type}
file size: {filedata.size}

    """
    )

    if await fileproses.SaveFile(
        filedata,
        filedata.filename,
        "tmp",
        ["text/plain", "text/markdown", "image/jpeg", "image/png", "application/pdf"],
    ):
        return {"message": "File telah di simpan"}
    else:
        return {"message": "file gagal di simpan"}

    # await saveFile_old(filedata, filedata.filename, "tmp", "txt")
    # await fileproses.SaveFile(
    # filedata.filename, filedata, "tmp/fileUpload", ["text/plain"]
    # )
    # print(f"namaFile {filedata.filename}")
    # await fileproses.SaveFile(filedata, filedata.filename, "tmp", {"txt": "txt/plain"})

    return {"detail": "aaaaaa"}
    # status, saved_filename = await saveFile(file)
    # if status:
    #     return {"filename": saved_filename}
    # else:
    #     return {"detail":"Upload Failed"}


import httpx


@router.get("/testOutSideReq")
def reqOutSide():
    r = httpx.get("http://api.weatherapi.com/v1/current.json")

    datarespon = {"status": r.status_code, "massege": r.json()}

    return {"message": datarespon}


@router.get("/testEnv")
def testEnv():
    print(GetEnv("asd"))
    return {"message": "hello world"}


from APP.config.utility.humanTime import GetTimeNow


@router.get("/testTime")
def gettimeini():
    # print(f"jalankan data {Get_time_by(by=timeBy.humanreadble)}")
    GetTimeNow().addOffset(7)
    data = f"""=== === === === === === === === === === === === === === ===
    waktu sekarang: {GetTimeNow().Human().getResult()}
    waktu sekarang +7: {GetTimeNow().addOffset(7).Human().getResult()}
    waktu +10 jam : {GetTimeNow().addTime(10,"H").getResult()}
    waktu +4+4 jam +10 menit: {GetTimeNow().addTime(4,"H").Human().addTime(10,"M").addTime(4,"H").getResult()}
    waktu Timestamp: {GetTimeNow().Timestamp(False).getResult()}

=== === === === === === === === === === === === === === ===
"""

    # print(GetTimeNow().addTime(10,"H").Human().getResult())
    print(data)

    # print(datetime.tzinfo)

    return {"message": data}


@router.get("/addTime")
def addTimeini():
    GetTimeNow().addOffset(5)
    return {"message": "hello world"}
