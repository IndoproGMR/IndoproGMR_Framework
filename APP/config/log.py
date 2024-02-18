# LOG
from fastapi import BackgroundTasks
import datetime
from APP.config.dotenvfile import getenvval


def LogProses(data: str):
    try:
        writeToLog(data)
        if getenvval("Log.print", "False") == "True":
            print(data)
    except Exception as e:
        print(f"Error writing to log: {e}")


def writeToLog(data):
    # Waktu sekarang dalam format yang mudah dibaca manusia
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    LogName = datetime.datetime.now().strftime("%Y-%m-%d")

    with open(
        f"log/{LogName}.log", mode="a"
    ) as logFile:  # Gunakan mode "a" untuk menambahkan log ke file yang ada
        content = (
            f"{current_time}: {data}\n"  # Menambahkan data yang akan dicatat dalam log
        )
        logFile.write(content)
