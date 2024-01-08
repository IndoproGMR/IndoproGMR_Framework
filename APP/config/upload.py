from typing import Union
from pathlib import Path
from APP.config.dotenvfile import getenvval

import secrets
import shutil


# file type list
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types


async def saveFile(
    file,
    filename: Union[str, None] = None,
    Path_FOLDER: Union[str, None] = None,
    file_type: Union[str, None] = None,
):
    # filter file yang tidak diperbolehkan
    if file_type is not None:
        if file.content_type != file_type:
            return False, None

    # Mengatur folder tempat menyimpan file
    UPLOAD_FOLDER = Path(getenvval("Folder.Upload.Path"))  # type: ignore

    if Path_FOLDER is None:
        # menggunakan default folder
        folder_Path = UPLOAD_FOLDER
    else:
        # menambahkan folder default dan Path_FOLDER
        folder_Path = UPLOAD_FOLDER.joinpath(Path_FOLDER)

    # membuat folder jika belum ada
    folder_Path.mkdir(parents=True, exist_ok=True)

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
    file_path = folder_Path / filename  # type: ignore
    # print(file_path)

    try:
        # Menyimpan file ke server
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            # file.close()
        return True, filename
    except Exception as e:
        print(e)
        # file.close()
        return False, None
