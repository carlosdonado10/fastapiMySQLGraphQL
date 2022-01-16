from fastapi import FastAPI
from sqlmodel import SQLModel

import uvicorn

from router import router
from settings import settings
from utils import get_db, engine
from models import *

app = FastAPI()

app.include_router(router)


@app.get('/')
def root():
    return 'hello world'


if __name__ == '__main__':
    SQLModel.metadata.create_all(engine)
    uvicorn.run('main:app', host=settings.backend_debug_host, port=settings.backend_debug_port)
