from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pokeapp.database.connection import get_db
from pokeapp.repository.respository import register_user, autenticate_user
from pokeapp.schemas.schemas import UserPublic, UserSchema, Token
from fastapi.security import OAuth2PasswordRequestForm
from pokeapp.security import get_current_user, create_access_token
import requests

router = APIRouter(prefix="/api")

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon"

@router.get("/")
async def get_all_pokemons(
    current_user=Depends(get_current_user),
    limit: int = 6,
    offset: int = 0
):
    try:
        response = requests.get(f"{POKEAPI_URL}?limit={limit}&offset={offset}")
        response.raise_for_status()
        pokemons = response.json()
        return pokemons
    except requests.exceptions.RequestException as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.post("/register", status_code=HTTPStatus.CREATED, response_model=UserPublic)
async def create_user(
    user: UserSchema,
    session: Session = Depends(get_db),
):
    new_user = register_user(session, user.username, user.password)
    return new_user


@router.post("/login", response_model=Token)
async def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_db)
):
    user = autenticate_user(
        session, username=form_data.username, password=form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data_payload={"sub": user.username})

    return {"access_token": access_token, "token_type": "Bearer"}
