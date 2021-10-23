from fastapi import FastAPI
import uvicorn
from .database import engine
from . import schemas, models
from .routers import movie


app = FastAPI()

models.Base.metadata.create_all(bind= engine)

app.include_router(movie.router)

