from fastapi import FastAPI
import uvicorn
from .database import engine
from . import schemas, models


app = FastAPI()

models.Base.metadata.create_all(bind= engine)


