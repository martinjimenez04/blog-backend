# Blog API

REST API for personal blog with categories and posts.

## Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic

## Features

- Categories management
- Posts CRUD with slug-based URLs
- Draft/published status
- Lazy loading (preview vs full content)

## Installation
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env`:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/blog_db
```

Run migrations:
```bash
alembic upgrade head
```

Start server:
```bash
uvicorn main:app --reload
```

API docs: `http://localhost:8000/docs`

## Endpoints

- `GET /categories` - List categories
- `POST /categories` - Create category
- `GET /posts` - List posts (preview)
- `GET /posts/{slug}` - Get post detail
- `POST /posts` - Create post
- `PUT /posts/{slug}` - Update post
- `DELETE /posts/{slug}` - Delete post