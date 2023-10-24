from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from APP.model.Occupation import CountOccupation, bySleepDuration
from APP.config.View import view

template = Jinja2Templates(directory="web/")


app = FastAPI()

app.mount("/css", StaticFiles(directory="web/css"), name="css")
app.mount("/js", StaticFiles(directory="web/js"), name="js")
app.mount("/img", StaticFiles(directory="web/img"), name="img")


app.add_middleware(
    CORSMiddleware,
    allow_origins={"*"},
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Route
@app.get("/", response_class=HTMLResponse)
async def run(request: Request):
    data = [{"test": "isi data"}]
    return view(request, "view/test.html", data)


@app.get("/api")
def read_root(request: Request):
    return {
        "client_host": request.client.host,  # type: ignore
        "client_Port": request.client.port,  # type: ignore
        "request_url": request.url.path,
    }


@app.get("/api/Occupation")
def Occupation():
    return CountOccupation()
