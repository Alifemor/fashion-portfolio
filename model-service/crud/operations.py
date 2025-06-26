# crud/operations.py

from sqlalchemy.orm import Session
from models.db_models import ShoeModel
import schemas
from core.config import settings
import redis


# Подключение к Redis
r = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)


def create_model(db: Session, model: schemas.ShoeModelCreate, photo_urls: list[str]):
    db_model = ShoeModel(
        name=model.name,
        description=model.description,
        tags=model.tags,
        photo_urls=photo_urls,
    )
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model


def get_models(db: Session):
    return db.query(ShoeModel).all()


def get_model(db: Session, model_id: int):
    return db.query(ShoeModel).filter(ShoeModel.id == model_id).first()

def delete_model(db: Session, model_id: int):
    model = db.query(ShoeModel).filter(ShoeModel.id == model_id).first()
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")

    db.delete(model)
    db.commit()

