from fastapi import FastAPI
from routers import saunas
from db import driver

app = FastAPI()
driver.init()

app.include_router(router=saunas.router, prefix="/saunas")
