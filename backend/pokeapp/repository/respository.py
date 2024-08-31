from http import HTTPStatus
from sqlalchemy.orm import Session
from sqlalchemy import select
from ..models.models import User
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from backend.pokeapp.security import get_password_hash, verify_password


def register_user(session: Session, username: str, password: str):
    try:
        db_user = User(username=username, password=get_password_hash(password))
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user
    except IntegrityError:
        session.rollback()
        raise HTTPException(
            status_code=400, detail="Usuário e/ou e-mail já cadastrados"
        )
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"{e}")


def autenticate_user(session: Session, username: str, password: str):
    user = session.scalar(select(User).where(User.username == username))
    if not user or not verify_password(password, user.password):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail="Usuário ou senha incorretos"
        )
    return user
