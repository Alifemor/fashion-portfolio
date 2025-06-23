# crud/crud.py

from sqlalchemy.orm import Session
from backend import models, schemas
from backend.core.config import settings
import redis

# Подключение к Redis
r = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)

def create_model(db: Session, model: schemas.ShoeModelCreate, photo_urls: list[str]):
    db_model = models.ShoeModel(
        name=model.name,
        description=model.description,
        tags=model.tags,
        photo_urls=photo_urls  # сохраняем ссылки из Redis
    )
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model
