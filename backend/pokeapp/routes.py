from http import HTTPStatus
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.pokeapp.database.connection import get_db
from backend.pokeapp.repository.respository import register_user
from backend.pokeapp.schemas.schemas import UserPublic, UserSchema

router = APIRouter(prefix='/api')

@router.get('/')
def message():
    return {'message':'Olá mundo!'}

@router.post('/register', status_code=HTTPStatus.CREATED ,response_model=UserPublic)
async def create_user(user: UserSchema, database: Session = Depends(get_db)):
    new_user = register_user(database, user.username, user.password)
    return new_user

@router.post('/login', status_code=HTTPStatus.OK ,response_model=UserPublic)
def login(user: UserSchema):
    ...