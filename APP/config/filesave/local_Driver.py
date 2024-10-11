# vim:fileencoding=utf-8:foldmethod=marker

# System {{{

import io
import os
from os.path import isdir, isfile
from typing import Union
from pathlib import Path
import secrets
import shutil
import glob
import aiofiles
import mimetypes
from abc import ABC
import json
from fastapi.responses import StreamingResponse


from APP.config.dotenvfile import GetEnv
from APP.config.log import LogProses

# from APP.config.util import Get_time_now

from APP.config.utility.util import Get_time_now


from .BaseDriver import BaseDriver


class local_Driver(BaseDriver):
    def __init__(self, prefix_Path: str = ""):
        try:
            self.prefix_Path = prefix_Path
            self.safeDelete = GetEnv("File_SafeDelete", "True").str()

            folderrecycle = GetEnv("File_recyclebin", f"SpecialDir/recyclebin").str()
            self.recyclebin = folderrecycle
            self.recyclebin_time = "%Y%m%d_%H%M%S_%f"

        except Exception as e:
            print(e)

    async def SaveFile(
        self, file, file_name: str, file_path: str = "", filter_types=[], save_mode="wb"
    ):
        try:
            # full_path = Path.joinpath(self.prefix_Path, file_path)
            # full_path.mkdir(exist_ok=True)

            full_path = os.path.join(self.prefix_Path, file_path, file_name)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)

            full_path = Path(full_path)

            if isinstance(file, str):
                file = file.encode("utf-8")

                with open(full_path, save_mode) as buffer:
                    buffer.write(file)
                return True

            else:
                if file.content_type not in filter_types:
                    return False
                with full_path.open(save_mode) as buffer:
                    shutil.copyfileobj(file.file, buffer)
                return True

        except Exception as e:
            LogProses(f"Gagal Menyimpan File {file_name}: {e}")
            return False

    async def SaveFolder(self, folder_path: str):
        try:
            full_path = os.path.join(self.prefix_Path, folder_path)

            os.makedirs(full_path, exist_ok=True)

        except Exception as e:
            LogProses(f"Gagal Membuat Folder {folder_path}: {e}")

    async def DeleteFile(self, file_name: str, file_path: str):
        try:
            full_path = os.path.join(self.prefix_Path, file_path, file_name)
            recyclebin = os.path.join(
                self.recyclebin, Get_time_now(self.recyclebin_time)
            )

            if self.safeDelete == "True":
                await self.MoveFile(
                    file_name,
                    os.path.join(self.prefix_Path, file_path),
                    recyclebin,
                )

            else:
                if os.path.exists(full_path):
                    os.remove(full_path)
                    LogProses(f"File berhasil di hapus {file_name}")
                else:
                    LogProses(f"File tidak Ditemukan {file_name}")

        except Exception as e:
            LogProses(f"Gagal Menghapus file {file_name}: {e}")

    async def DeleteFolder(
        self, folder_path: str, recursive: bool = False, deleteWithContent=False
    ):
        try:
            full_path = os.path.join(self.prefix_Path, folder_path)
            recyclebin = os.path.join(
                self.recyclebin, Get_time_now(self.recyclebin_time)
            )

            if "*" in full_path or "?" in full_path:
                paths = glob.glob(full_path)

                if not paths:
                    LogProses(
                        f"tidak ada file atau folder yang di temukan dengan wildcard: {folder_path}"
                    )
                    return

                for path in paths:
                    if os.path.isfile(path):
                        file_name = os.path.basename(path)
                        if self.safeDelete == "True":
                            await self.MoveFile(
                                file_name,
                                os.path.dirname(path),
                                recyclebin,
                            )

                        else:
                            os.remove(path)

                    elif os.path.isdir(path):
                        if self.safeDelete == "True":
                            folder_name = os.path.basename(path)
                            await self.MoveFile(
                                folder_name,
                                os.path.dirname(path),
                                recyclebin,
                            )

                        else:
                            await self.DeleteFolder(
                                os.path.relpath(path, self.prefix_Path),
                                recursive=recursive,
                                deleteWithContent=deleteWithContent,
                            )
            else:

                if not os.path.exists(full_path):
                    LogProses(f"folder tidak Ditemukan {folder_path}")
                    return

                if deleteWithContent:
                    if self.safeDelete == "True":
                        await self.MoveFile(
                            os.path.basename(full_path),
                            os.path.dirname(full_path),
                            recyclebin,
                        )

                    else:
                        shutil.rmtree(full_path)
                        LogProses(f"folder {folder_path} dan isinya berhasil di hapus")

                elif recursive:
                    # Menghapus folder secara rekursif, tapi hanya jika isinya adalah folder kosong
                    for root, dirs, files in os.walk(full_path, topdown=False):
                        if files:
                            LogProses(
                                f"Gagal menghapus secara recursive, folder {root} berisi file"
                            )
                        return
                    # Setelah pengecekan, hapus folder secara recursive
                    os.removedirs(full_path)
                    LogProses(f"Folder {folder_path} berhasil dihapus secara recursive")

                else:
                    os.rmdir(full_path)
                    LogProses(f"folder {folder_path} berhasil di hapus")

        except Exception as e:
            LogProses(f"gagal Menghapus folder {folder_path}: {e}")

    async def ReadFile(self, file_name: str, file_path: str = "", file_mode="r"):
        try:
            full_path = os.path.join(self.prefix_Path, file_path, file_name)

            # Cek apakah file ada
            if not os.path.exists(full_path):
                raise FileNotFoundError(f"{file_name} tidak ditemukan di {file_path}")

            # Dapatkan tipe MIME untuk menentukan apakah file biner atau teks
            mime_type, _ = mimetypes.guess_type(full_path)
            if mime_type:
                main_type = mime_type.split("/")[0]
            else:
                main_type = None

            # Jika file teks (txt, csv, json), baca dalam mode teks
            if main_type == "text" or file_mode == "r":
                async with aiofiles.open(full_path, mode=file_mode) as file:
                    content = await file.read()

                # Jika file adalah JSON, coba parse kontennya
                if mime_type == "application/json":
                    try:
                        # Parsing JSON
                        parsed_data = json.loads(content)
                        return parsed_data
                    except json.JSONDecodeError as e:
                        LogProses(f"Error parsing JSON file {file_name}: {e}")
                        return {"error": f"Invalid JSON format: {str(e)}"}
                else:
                    return content

            # Jika file biner (pdf, gambar), baca dalam mode biner
            elif (
                main_type == "application" or main_type == "image" or file_mode == "rb"
            ):
                async with aiofiles.open(full_path, mode="rb") as file:
                    content = await file.read()

                return StreamingResponse(io.BytesIO(content), media_type=mime_type)

            else:
                raise ValueError(
                    f"Tipe file {file_name} tidak dikenali untuk pembacaan."
                )

        except Exception as e:
            LogProses(f"Gagal membaca file {file_name}: {e}")
            return None

    # Fungsi untuk menyalin file
    async def CopyFile(
        self, src_file_name: str, src_file_path: str, dest_file_path: str
    ):
        try:
            src_full_path = os.path.join(self.prefix_Path, src_file_path, src_file_name)
            dest_full_path = os.path.join(
                self.prefix_Path, dest_file_path, src_file_name
            )

            # Menyalin file ke destinasi baru
            shutil.copy2(src_full_path, dest_full_path)

        except Exception as e:
            LogProses(
                f"Gagal menyalin file dari {src_file_path} ke {dest_file_path}: {e}"
            )

    # Fungsi untuk memindahkan file
    async def MoveFile(
        self, src_file_name: str, src_file_path: str, dest_file_path: str
    ):
        try:
            src_full_path = os.path.join(self.prefix_Path, src_file_path, src_file_name)
            dest_full_path = os.path.join(
                self.prefix_Path, dest_file_path, src_file_name
            )
            if not os.path.exists(os.path.join(self.prefix_Path, dest_file_path)):
                os.makedirs(os.path.join(self.prefix_Path, dest_file_path))

            # Memindahkan file ke destinasi baru
            shutil.move(src_full_path, dest_full_path)

        except Exception as e:
            LogProses(
                f"Gagal memindahkan file dari {src_file_path} ke {dest_file_path}: {e}"
            )

    async def ListFile(self, file_path: str):
        pass

    # async def saveFileClient(
    #     self,
    #     prefix_name:srt="",
    #     file_name_raw:str,
    #     file_path:str="",
    #     filter_types = [],
    #     file_content
    # ):
    #     file_name_raw
    #     for types in filter_types:
    #         if
    #


# }}}


# System {{{


# file type list
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types


async def saveFile_old(
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
    UPLOAD_FOLDER = Path(GetEnv("Folder.Upload.Path", "SpecialDir/UploadDir").str())

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
        with file_path.open("wb", flush=True) as buffer:
            shutil.copyfileobj(file.file, buffer)
            # file.close()
        return True, filename
    except Exception as e:
        print(e)
        # file.close()
        return False, None


async def readFile(loc):
    # Mengatur folder tempat menyimpan file
    UPLOAD_FOLDER = Path(getenvval("Folder.Upload.Path", "uploadFolder"))  # type: ignore
    # cek apakah file ada ?
    if UPLOAD_FOLDER.joinpath(loc).exists():
        # baca file
        with UPLOAD_FOLDER.joinpath(loc).open("rb") as f:
            return True, f.read()
    else:
        return False, None


# }}}
