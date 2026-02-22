from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    slug = Column(String(100), nullable=False, unique=True, index=True)
    
    # Relación: una categoría tiene muchos posts
    posts = relationship("Post", back_populates="category")
    
    def __repr__(self):
        return f"<Category {self.name}>"