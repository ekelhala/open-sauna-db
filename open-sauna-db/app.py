from fastapi import FastAPI
from routers import saunas, reviews, auth
from db import driver

app = FastAPI()
driver.init()

app.include_router(router=saunas.router, prefix="/saunas")
app.include_router(router=reviews.router, prefix="/reviews")
app.include_router(router=auth.router, prefix="/auth")
