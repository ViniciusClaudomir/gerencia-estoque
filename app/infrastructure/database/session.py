from app.core.logger import logger
from app.exceptions.config_invalid_database import DBConfigurationError

from  typing import Generator
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base, Session
import os
from contextlib import contextmanager


DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_SCHEMA = os.getenv("DATABASE_SCHEMA")

if not all([DATABASE_URL, DATABASE_SCHEMA, DATABASE_PASSWORD, DATABASE_PORT, DATABASE_USER]):
    raise DBConfigurationError('')


DATABASE_URL = (
    f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_URL}:{DATABASE_PORT}/{DATABASE_SCHEMA}"
)

# Engine
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()

@contextmanager
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.erro(e)
        logger.error("Error connecting to database")
        db.close()

def get_table_info(session: Session):
    inspector = inspect(session.bind)
    tables = inspector.get_table_names()
    
    table_info = {}
    for table_name in tables:
        columns = inspector.get_columns(table_name)
        table_info[table_name] = [x['name'] for x in columns]

    return table_info