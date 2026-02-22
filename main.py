from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import categories, posts

app = FastAPI(
    title="Blog API",
    description="REST API para blog personal con categorías y posts",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # (permite que React llame a fastAPI)
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