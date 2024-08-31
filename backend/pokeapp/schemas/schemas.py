from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    password: str

class UserPublic(BaseModel):
    username: str