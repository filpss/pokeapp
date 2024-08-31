from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = config("DB_URL")

engine = create_engine(DB_URL, pool_pre_ping=True)

Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
