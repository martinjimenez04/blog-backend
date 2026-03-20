from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import categories, posts
from dotenv import load_dotenv
import os

load_dotenv()


def _get_allowed_origins() -> list[str]:
    cors_origins = os.getenv("CORS_ORIGINS", "")
    parsed = [origin.strip() for origin in cors_origins.split(",") if origin.strip()]

    # Default local frontend for development.
    if not parsed:
        parsed = ["http://localhost:3000"]

    return parsed

app = FastAPI(
    title="Blog API",
    description="REST API para blog personal con categorías y posts",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=_get_allowed_origins(),
    allow_credentials=True,
    allow_methods=["*"],    # (GET, POST, PUT, DELETE,...)
    allow_headers=["*"],    # (Content-Type, Authorization,...)
)

# Registrar routers
app.include_router(categories.router)
app.include_router(posts.router)


@app.get("/")
def root():
    return {
        "mensaje": "Blog API funcionando ✓",
        "docs": "/docs"
    }