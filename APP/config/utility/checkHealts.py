from APP.config.log import LogProses
from APP.config.utility import randomGen
# from APP.config.util import Gen_Random_sha256

# from APP.config.manager
# from APP.config.manager import filemanager, sqlmanager, cachemanager

from APP.config.manager import filemanager


def checkHealth():
    cH_fileProses()

    # pass


def cH_fileProses():
    fileProses = filemanager.create("tmp/")

    await fileProses.SaveFile("","","",[],save_mode="w")

    # fileProses = filemanager.create("tmp/")

    # menyimpan file
    # fileProses.SaveFile(file_name="", file_path="", file_mode="w", file_content="")

    # fileProses.SaveFolder("")

    try:
        namaFolder = randomGen.Gen_Random_sha256()
        namaFile = randomGen.Gen_Random_sha256()
        dataFile = randomGen.Gen_Random_sha256()

        # membuat random str
        # test membuat folder pada tmp dengan nama random str
        # cek apakah bisa membuka folder random str
        # cek apakah ada file di dalam folder random str ?
        # bila kosong
        # test membuat file dengan random str
        # cek apakah file ada ?
        # bila ada apakah bisa di baca ?
        # bila isi nya kosong
        # isi file tersebut dengan random str dengan beberapa 10 line
        # lalu cek apakah isi file tersebut ada sama dengan random data

        # bila sama maka tidak ada masalah
        pass
        LogProses("checkHealth_localFile Berhasil", True)
    except Exception as e:
        LogProses(f"checkHealth_localFile gagal: {e}", True)
        raise e


def cH_sql():
    pass


def cH_cache():
    pass
