import inspect
import os

import aiofiles

# from asyncio.base_events import os

# from fastapi import Path

from APP.config.dotenvfile import GetEnv
from APP.config.utility.util import Get_time_now


def _getLine(stack_in: int = 2):
    return inspect.stack()[stack_in].lineno


def _getFilename(stack_in: int = 2):
    return f"{inspect.stack()[stack_in].filename.split('/')[-2]}/{inspect.stack()[stack_in].filename.split('/')[-1]}"
    # return inspect.stack()[stack_in].filename.split("/")[-1]


def _getFunction():
    return inspect.stack()[2].function


def _getTime(timeformat: str):
    return Get_time_now(timeformat)


def _getLogFilename(timeformat: str, prifixName: str):
    return f"{Get_time_now(timeformat)}{prifixName}"


# def _getFormatedContent():


def LogProses(data: str, forcePrint=False, prifixName: str = "") -> None:
    try:
        current_time = _getTime(GetEnv("Log_time", "%H:%M:%S.%f").str())
        LogName = _getLogFilename(GetEnv("Log_filename", "%Y-%m-%d").str(), prifixName)

        module_name = _getFilename()
        line_number = _getLine()

        content_data = (
            f"{current_time}: [Fn:({module_name}) Ln:({line_number})]: {data}\n"
        )

        if GetEnv("Log_print", "False").is_("True") or forcePrint:
            print(content_data)

        # simpan data ke file
        try:
            with open(f"log/{LogName}.log", mode="a") as file:
                file.write(content_data)

        except Exception as e:
            print(f"gagal menyimpan Log. isi LOG:\n{data}")

    except Exception as e:
        print(f"Error writing to log: {e}")


def debugProses(data: str, note: str = "", prifixName: str = "") -> None:
    if GetEnv("Log_debug_active", "False").is_("False"):
        return

    try:
        if not os.path.exists("log/debug"):
            os.mkdir("log/debug")
        # print("full", list(inspect.stack()))
        # print("test 1", inspect.stack()[3].filename.split()[-1])

        current_time = _getTime(GetEnv("Log_time", "%H:%M:%S.%f").str())
        LogName = _getLogFilename(GetEnv("Log_filename", "%Y-%m-%d").str(), prifixName)

        function_name = _getFunction()

        # content_data = f"{current_time}: (DEBUG) [{module_name} ({line_number}),{function_name}()]: {data}\n"

        content_data = f""">====================<
{'(DEBUG)':^20}
{current_time:^20}
[
({_getFilename()}, {_getLine()}),
({_getFilename(3)}, {_getLine(3)}),
({_getFilename(4)}, {_getLine(4)}),
]
{function_name}()
data: {data}
note: {note}
<====================>"""

        print(content_data)

        # simpan data ke file
        try:
            # async with aiofiles.open(f"log/{LogName}.log",mode="a") as f:
            # await f.write(content_data)
            with open(f"log/debug/{LogName}.log", mode="a") as file:
                file.write(content_data)

        except Exception as e:
            print(f"gagal menyimpan Log. isi LOG:\n{data}")

    except Exception as e:
        print(f"Error in debugProses: {e}")
