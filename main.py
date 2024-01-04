import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from APP.config.dotenvfile import getenvval

from APP.routers import test


app = FastAPI(
    # docs_url=None,
    # redoc_url=None,
    # openapi_prefix="/api/v1",
    responses={404: {"description": "Not found"}},
)

app.mount("/asset/css", StaticFiles(directory="public/css"), name="css")
app.mount("/asset/js", StaticFiles(directory="public/js"), name="js")
app.mount("/asset/img", StaticFiles(directory="public/img"), name="img")

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins={"*"},
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route
app.include_router(test.router)

# if __name__ == "__main__":
#     config = uvicorn.Config(
#         "main:app",
#         host=getenvval("link.base", default="0.0.0.0"),  # type: ignore
#         port=int(getenvval("link.port.API", default=8000)),  # type: ignore
#         log_level="info",  # type: ignore
#         # reload=True,
#     )
#     server = uvicorn.Server(config)
#     server.run()
