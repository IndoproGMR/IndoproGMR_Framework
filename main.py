import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


from APP.routers import test


app = FastAPI()

app.mount("/css", StaticFiles(directory="public/css"), name="css")
app.mount("/js", StaticFiles(directory="public/js"), name="js")
app.mount("/img", StaticFiles(directory="public/img"), name="img")

app.add_middleware(
    CORSMiddleware,
    allow_origins={"*"},
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route
app.include_router(test.router)

if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=8000)
    server = uvicorn.Server(config)
    server.run()
