from pydantic import BaseModel
from datetime import datetime
from app.schemas.category import CategoryResponse


class PostBase(BaseModel):
    title: str
    slug: str
    excerpt: str
    content: str
    category_id: int
    published: bool = False


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    title: str | None = None
    excerpt: str | None = None
    content: str | None = None
    category_id: int | None = None
    published: bool | None = None


# Schema para la lista (sin content completo)
class PostPreview(BaseModel):
    id: int
    title: str
    slug: str
    excerpt: str
    published: bool
    created_at: datetime
    category: CategoryResponse  # incluye la categoría
    
    class Config:
        from_attributes = True


# Schema para vista individual (con content completo)
class PostDetail(PostPreview):
    content: str
    updated_at: datetime