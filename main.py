from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import time

# !add more Route
from APP.routers import test
from APP.routers import demo

app = FastAPI(
    # docs_url=None,
    # redoc_url=None,
    responses={404: {"description": "Not found"}},
)

app.mount("/asset/css", StaticFiles(directory="public/css"), name="css")  # type: ignore
app.mount("/asset/js", StaticFiles(directory="public/js"), name="js")  # type: ignore
app.mount("/asset/img", StaticFiles(directory="public/img"), name="img")  # type: ignore

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins={"*"},
    allow_methods=["*"],
    allow_headers=["*"],
)


# !Route
app.include_router(test.router)
app.include_router(demo.router)

# !prosess time pada middleware


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
