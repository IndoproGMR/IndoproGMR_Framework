import shutil
from typing import Annotated
import secrets
from fastapi import UploadFile
from typing import Union
import shutil
from pathlib import Path

from sqlalchemy import false, true

# Mengatur folder tempat menyimpan file
UPLOAD_FOLDER = Path("uploadFolder")


def saveFile(file, filename: Union[str, None] = None):
    # Pastikan folder uploadFolder sudah ada
    UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

    if filename is None:
        # Jika tidak ada nama file yang diberikan, maka gunakan random string
        filename = secrets.token_hex(16)
        # tambahan file extention
        filename = filename + "." + file.filename.split(".")[-1]  # type: ignore
    else:
        # Jika ada nama file yang diberikan, maka gunakan nama file yang diberikan
        filename = filename
        # Ganti nama file jika ada spasi
        filename = filename.replace(" ", "_")
        # Ganti nama file jika ada tanda baca
        filename = filename.replace(":", "_")
        # Ganti nama file jika ada tanda koma
        filename = filename.replace(",", "_")
        # # Ganti nama file jika ada tanda titik
        # filename = filename.replace(".", "_")
        # Ganti nama file jika ada tanda garis miring
        filename = filename.replace("-", "_")

    # Gabungkan path file untuk disimpan
    file_path = UPLOAD_FOLDER / filename  # type: ignore

    try:
        # Menyimpan file ke server
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            # file.close()
        return true
    except Exception as e:
        print(e)
        file.close()
        return false
