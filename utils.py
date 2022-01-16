from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from settings import settings
from contextlib import contextmanager
from typing import Generator


engine = create_engine(settings.sql_connection_string)
session_maker = sessionmaker(autocommit=False, expire_on_commit=False, autoflush=False, bind=engine)


@contextmanager
def get_db() -> Generator:
    with session_maker() as session:
        with session.begin():
            try:
                yield session
            finally:
                session.close()
