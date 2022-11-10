from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apis.users import router as users_router

# Creating FastAPI app
app = FastAPI(
    title="BHub Project API",
    description="An API built for the BHub admission process.",
    version="1.0.0",
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
