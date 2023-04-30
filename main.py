from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from rentproject.API import user, search

app = FastAPI()
app.include_router(user.router)
app.include_router(search.router)
app.mount("/", StaticFiles(directory="static", html=True), name="static")
