from http import HTTPStatus
from fastapi.security import OAuth2PasswordBearer
from jwt import decode, encode
from jwt.exceptions import PyJWTError
from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone
from decouple import config
from sqlalchemy import select
from pokeapp.database.connection import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from pokeapp.models.models import User
from pokeapp.redis_client import redis_client

pwd_context = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(clean_password: str, hashed_password: str):
    return pwd_context.verify(clean_password, hashed_password)


def create_access_token(data_payload: dict):
    to_encode = data_payload.copy()

    expire = datetime.now(tz=timezone.utc) + timedelta(
        minutes=int(config("ACCESS_TOKEN_EXPIRE_MINUTES"))
    )

    to_encode.update({"exp": expire})
    encode_jwt = encode(to_encode, config("SECRET_KEY"), algorithm=config("ALGORITHM"))
    return encode_jwt


async def get_current_user(
    session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode(token, config("SECRET_KEY"), algorithms=config("ALGORITHM"))
        username: str = payload.get("sub")
        if not username:
            raise credentials_exception

        cached_token = redis_client.get(f"user_session_{username}")
        if not cached_token:
            raise credentials_exception

        if cached_token.decode("utf-8") != token:
            raise credentials_exception

    except PyJWTError:
        raise credentials_exception

    user_db = session.scalar(select(User).where(User.username == username))

    if not user_db:
        raise credentials_exception

    return user_db
