from fastapi import FastAPI
from backend.pokeapp.routes import router
from database.base import Base
from database.connection import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
