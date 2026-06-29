from sqlite3 import dbapi2
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

# this is the db engine. its role is to maintain the connection to the database.
engine = create_engine(settings.database_url)

# this is the session factory.session factory is called once but sessions are created as per the number of requests. its role is to create a session object.
SessionFactory = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

# this is the base class for all the models.
class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close