from ast import Num
import os
from dotenv import load_dotenv

load_dotenv()


def getenvval(name: str, default=""):
    return os.getenv(name, default)
