from fastapi import FastAPI
from routers import saunas

app = FastAPI()

app.include_router(router=saunas, prefix="/saunas")
