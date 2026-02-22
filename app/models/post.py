from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    slug = Column(String(200), nullable=False, unique=True, index=True)
    excerpt = Column(Text, nullable=False)  # resumen corto
    content = Column(Text, nullable=False)  # contenido completo
    published = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign key a categoría
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    
    # Relación: cada post pertenece a una categoría
    category = relationship("Category", back_populates="posts")
    
    def __repr__(self):
        return f"<Post {self.title}>"