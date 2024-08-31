from sqlalchemy.orm import Session
from ..models.models import User
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from backend.pokeapp.security import get_password_hash

def register_user(database: Session, username: str, password: str):
    try:
        db_user = User(username=username, password=get_password_hash(password))
        database.add(db_user)
        database.commit()
        database.refresh(db_user)
        return db_user
    except IntegrityError:
        database.rollback()
        raise HTTPException(
            status_code=400,
            detail="Usuário e/ou e-mail já cadastrados"
        )
    except Exception as e:
        database.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"{e}")
