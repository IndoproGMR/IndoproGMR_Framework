from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

# from config.conn import *

from model.Occupation import CountOccupation, bySleepDuration


app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Route
@app.get("/")
def read_root(request: Request):
    return {
        "client_host": request.client.host,  # type: ignore
        "client_Port": request.client.port,  # type: ignore
        "request_url": request.url.path,
    }
    # return {"Hello": "World"}


@app.get("/api/Occupation")
def Occupation():
    return CountOccupation()
