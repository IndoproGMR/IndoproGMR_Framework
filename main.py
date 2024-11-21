# vim:fileencoding=utf-8:foldmethod=marker

# version check {{{

import platform
import sys

from APP.config.log import LogProses

# }}}

# @INFO

# System {{{
# INFO import packed

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.exceptions import HTTPException

from APP.config.dotenvfile import GetEnv


async def not_found_error(request: Request, exc: HTTPException):
    return RedirectResponse(
        GetEnv("link_error_500", "https://fastapi.tiangolo.com").str()
    )
    # return RedirectResponse(Link_not_found_error)


async def internal_error(request: Request, exc: HTTPException):
    return RedirectResponse(
        GetEnv("link_error_404", "https://fastapi.tiangolo.com").str()
    )
    # return RedirectResponse(Link_internal_error)


exception_handlers = {404: not_found_error, 500: internal_error}


app = FastAPI(
    # docs_url=None,
    # redoc_url=None,
    # exception_handlers=exception_handlers
)


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


# }}}

# userCode {{{


# from APP.config.cron import scheduler
from APP.config.manager import filemanager

fileproses = filemanager.create("")


# Mulai scheduler ketika aplikasi FastAPI mulai berjalan
@app.on_event("startup")
async def startup_event():
    # Mendapatkan versi Python saat ini
    PY_VER = platform.python_version_tuple()

    # Memastikan versi minimal Python adalah 3.10.10
    if (int(PY_VER[0]), int(PY_VER[1]), int(PY_VER[2])) <= (3, 10, 10):
        print("Versi Python terlalu rendah. Minimal versi 3.10.10 diperlukan.")
        sys.exit()  # Pastikan menggunakan sys.exit() untuk menghentikan program


    LogProses("startup_event")
    if GetEnv("File_CleanTmpOnBoot", "False").is_("True"):
        await fileproses.DeleteFolder("tmp/*", deleteWithContent=True)
        # pass
    # scheduler.start()


# Matikan scheduler ketika aplikasi berhenti
@app.on_event("shutdown")
def shutdown_event():
    LogProses("shutdown_event")
    # quit()
    pass
    # scheduler.shutdown()


# INFO Untuk mengatur lokasi asset untuk laman html
app.mount("/asset/css", StaticFiles(directory="UserCode/assets/css"), name="css")
app.mount("/asset/js", StaticFiles(directory="UserCode/assets/js"), name="js")
app.mount("/asset/img", StaticFiles(directory="UserCode/assets/img"), name="img")


app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# INFO add more Route


from UserCode.routers import Demo_Database
from UserCode.routers import Demo_Cache
from UserCode.routers import Demo_FrontEnd
from UserCode.routers import Demo_filesystem

from UserCode.routers import Demo


# INFO Route lokasi

# app.include_router(test.router)
app.include_router(Demo.router)
app.include_router(Demo_Database.router)
app.include_router(Demo_Cache.router)
app.include_router(Demo_FrontEnd.router)
app.include_router(Demo_filesystem.router)


# INFO prosess time pada middleware

import time


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


# }}}
