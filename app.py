from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.sqlalchemy import Base, engine

from apis.users import router as users_router
from apis.banks import router as banks_router

# Initialize Base and create tables
Base.metadata.create_all(bind=engine)

# Creating FastAPI app
app = FastAPI(
    title="BHub Project API",
    description="An API built for the BHub admission process.",
    version="1.0.1",
    docs_url="/",
    redoc_url=None
)

# Adding CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Adding routers
app.include_router(users_router)
app.include_router(banks_router)