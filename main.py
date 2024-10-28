# vim:fileencoding=utf-8:foldmethod=marker

# @INFO

# System {{{
# INFO import packed

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.exceptions import HTTPException
import time

from APP.config.dotenvfile import GetEnv

# }}}

# userCode {{{


# INFO untuk mengirim user

Link_internal_error = "https://fastapi.tiangolo.com"
Link_not_found_error = "https://fastapi.tiangolo.com"


# }}}


# System {{{
async def not_found_error(request: Request, exc: HTTPException):
    return RedirectResponse(Link_not_found_error)


async def internal_error(request: Request, exc: HTTPException):
    return RedirectResponse(Link_internal_error)


exception_handlers = {404: not_found_error, 500: internal_error}


app = FastAPI(
    # docs_url=None,
    # redoc_url=None,
    # exception_handlers=exception_handlers
)


# INFO prosess time pada middleware
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

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
    if GetEnv("File_CleamTmpOnBoot", "False") == "True":
        await fileproses.DeleteFolder("tmp/*", deleteWithContent=True)
    # scheduler.start()


# Matikan scheduler ketika aplikasi berhenti
@app.on_event("shutdown")
def shutdown_event():
    pass
    # scheduler.shutdown()


# INFO Untuk mengatur lokasi asset untuk laman html
app.mount("/asset/css", StaticFiles(directory="UserCode/assets/css"), name="css")
app.mount("/asset/js", StaticFiles(directory="UserCode/assets/js"), name="js")
app.mount("/asset/img", StaticFiles(directory="UserCode/assets/img"), name="img")


app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins={"*"},
    allow_methods=["*"],
    allow_headers=["*"],
)

# INFO add more Route


from UserCode.routers import Demo_Database
from UserCode.routers import Demo_Cache
from UserCode.routers import Demo_FrontEnd

from UserCode.routers import Demo


# INFO Route lokasi

# app.include_router(test.router)
app.include_router(Demo.router)
app.include_router(Demo_Database.router)
app.include_router(Demo_Cache.router)
app.include_router(Demo_FrontEnd.router)


# }}}
