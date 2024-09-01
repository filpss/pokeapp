from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.pokeapp.database.connection import get_db
from backend.pokeapp.repository.respository import register_user, autenticate_user
from backend.pokeapp.schemas.schemas import UserPublic, UserSchema, Token
from fastapi.security import OAuth2PasswordRequestForm
from backend.pokeapp.security import get_current_user, create_access_token

router = APIRouter(prefix="/api")


@router.get("/")
async def message(
    session: Session = Depends(get_db), current_user=Depends(get_current_user)
):
    return {"message": "Olá mundo!"}


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
