# vim:fileencoding=utf-8:foldmethod=marker

# System {{{

import os
from dotenv import load_dotenv


load_dotenv()

#
# def getenvval(name: str, default: str = "") -> str:
#     return os.environ.get(name, default)
#

#
# def GetEnv(name: str, default: str | int = "", typeEnv: str = "str"):
#     value = os.environ.get(name, default)
#
#     try:
#         if typeEnv == "str":
#             return str(value)
#         elif typeEnv == "int":
#             return int(value)
#         else:
#             raise ValueError(f"Tipe data '{typeEnv}' tidak dikenali.")
#     except ValueError as e:
#         return default
#


class EnvVar:
    def __init__(self, value):
        self.value = value

    def str(self):
        return str(self.value)

    def int(self):
        try:
            return int(self.value)
        except ValueError:
            raise ValueError(f"Cannot convert '{self.value}' to int.")

    def float(self):
        try:
            return float(self.value)
        except ValueError:
            raise ValueError(f"Cannot convert '{self.value}' to float.")


# Fungsi GetEnv yang mengembalikan objek EnvVar
def GetEnv(name: str, default: str | int = "") -> EnvVar:
    value = os.environ.get(name, default)
    return EnvVar(value)


# }}}
