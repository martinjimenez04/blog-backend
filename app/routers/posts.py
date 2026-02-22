from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.post import PostCreate, PostUpdate, PostPreview, PostDetail
from app.models.post import Post
from app.database import get_db

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)


@router.get("/", response_model=List[PostPreview])
def get_posts(
    published_only: bool = True,
    db: Session = Depends(get_db)
):
    """
    Lista todos los posts (solo preview).
    Por defecto solo muestra los publicados.
    """
    query = db.query(Post)  
    
    if published_only:
        query = query.filter(Post.published == True)
    
    return query.order_by(Post.created_at.desc()).all()


@router.get("/{slug}", response_model=PostDetail)
def get_post(slug: str, db: Session = Depends(get_db)):
    """Obtiene un post completo por su slug"""
    post = db.query(Post).filter(Post.slug == slug).first()
    
    if not post:
        raise HTTPException(status_code=404, detail="Post no encontrado")
    
    return post


@router.post("/", response_model=PostDetail, status_code=201)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    """Crea un nuevo post"""
    # Verificar que el slug no exista
    existing = db.query(Post).filter(Post.slug == post.slug).first()
    if existing:
        raise HTTPException(status_code=400, detail="Ya existe un post con ese slug")
    
    new_post = Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post


@router.put("/{slug}", response_model=PostDetail)
def update_post(
    slug: str,
    post_update: PostUpdate,
    db: Session = Depends(get_db)
):
    """Actualiza un post existente"""
    post = db.query(Post).filter(Post.slug == slug).first()
    
    if not post:
        raise HTTPException(status_code=404, detail="Post no encontrado")
    
    # Actualizar solo los campos que llegaron
    campos = post_update.model_dump(exclude_unset=True)
    for key, value in campos.items():
        setattr(post, key, value)
    
    db.commit()
    db.refresh(post)
    
    return post


@router.delete("/{slug}", status_code=204)
def delete_post(slug: str, db: Session = Depends(get_db)):
    """Elimina un post"""
    post = db.query(Post).filter(Post.slug == slug).first()
    
    if not post:
        raise HTTPException(status_code=404, detail="Post no encontrado")
    
    db.delete(post)
    db.commit()
    
    return None