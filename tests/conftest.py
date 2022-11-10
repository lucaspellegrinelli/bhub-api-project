from typing import Generator, Any

import os
import pytest
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from core.sqlalchemy import Base, get_db

from apis.users import router as users_router

# Create the mock database engine
engine = create_engine(os.getenv("SQLALCHEMY_TESTING_DATABASE_URL"), connect_args={"check_same_thread": False})

# Create the mock database session
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def start_application() -> FastAPI:
    """
    Starts the application and returns the FastAPI app.
    """
    app = FastAPI()
    app.include_router(users_router)
    return app

@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
    """
    Create a fresh database on each test case.
    """
    Base.metadata.create_all(engine)
    _app = start_application()
    yield _app
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def db_session(app: FastAPI) -> Generator[SessionTesting, Any, None]:
    """
    Create a fresh database session on each test case.
    """
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionTesting(bind=connection)
    yield session # use the session in tests.
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(scope="function")
def client(app: FastAPI, db_session: SessionTesting) -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """

    def _get_test_db():
        try:
            yield db_session
        finally:
            pass
    
    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client