from fastapi import FastAPI
from backend.pokeapp.routes import router
from backend.pokeapp.database.base import Base
from backend.pokeapp.database.connection import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
