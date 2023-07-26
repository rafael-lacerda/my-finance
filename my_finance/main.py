from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from my_finance.routers import login, main, root

app = FastAPI()

app.include_router(login.router)
app.include_router(main.router)
app.include_router(root.router)

app.mount("/static", StaticFiles(directory="static"), name="static")
