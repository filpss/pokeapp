from sqlalchemy import Column, Integer, String
from backend.pokeapp.database.base import Base


class User(Base):
    __tablename__ = "tb_users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
