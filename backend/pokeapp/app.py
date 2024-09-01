from fastapi import FastAPI
from pokeapp.routes import router
from pokeapp.database.base import Base
from pokeapp.database.connection import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
