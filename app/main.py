from fastapi import FastAPI
from .database import engine
from . import models
from .routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo CRUD App")

app.include_router(router)
