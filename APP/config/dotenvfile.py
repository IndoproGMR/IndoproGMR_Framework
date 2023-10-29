import os
from dotenv import load_dotenv

load_dotenv()


def getenvval(name: str):
    return os.getenv(name)
