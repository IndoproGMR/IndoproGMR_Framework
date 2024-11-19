from abc import ABC, abstractmethod


"""
File Proses harus bisa

Menyimpan File
Membuat Folder

Menghapus File
Menghapus Folder

Memindahkan File
Memindahkan Folder

Membaca File
Membaca semuah File Yang ada didalam folder
Membaca semuah folder di dalam folder

men sanitation Nama
men random Nama




"""


class BaseDriver(ABC):

    @abstractmethod
    async def SaveFile(
        self,
        file,
        file_name: str,
        file_path: str = "",
        filter_types=[],
        save_mode: str = "wb",
    ) -> bool:
        pass

    @abstractmethod
    async def SaveFolder(self, folder_path: str):
        pass

    @abstractmethod
    async def DeleteFile(self, file_name: str, file_path: str):
        pass

    @abstractmethod
    async def DeleteFolder(
        self, folder_path: str, recursive: bool = False, deleteWithContent=False
    ):
        pass

    @abstractmethod
    async def ReadFile(self, file_name: str, file_path: str = "", file_mode="r"):
        pass

    @abstractmethod
    async def CopyFile(
        self, src_file_name: str, src_file_path: str, dest_file_path: str
    ):
        pass

    @abstractmethod
    async def MoveFile(
        self, src_file_name: str, src_file_path: str, dest_file_path: str
    ):
        pass

    @abstractmethod
    async def ListFile(self, file_path: str):
        pass

    # @abstractmethod
    # async def testNull(self):
    #     pass
