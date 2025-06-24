# crud/operations.py

from sqlalchemy.orm import Session
from models.db_models import ShoeModel, Review
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


def create_review(db: Session, model_id: int, review: schemas.ReviewCreate):
    db_review = Review(**review.dict(), shoe_model_id=model_id)
    db.add(db_review)

    # обновляем среднюю оценку и кол-во отзывов
    model = db.query(ShoeModel).filter(ShoeModel.id == model_id).first()
    if model:
        model.num_reviews += 1
        total_rating = model.avg_rating * (model.num_reviews - 1) + review.rating
        model.avg_rating = total_rating / model.num_reviews

    db.commit()
    db.refresh(db_review)
    return db_review


def get_reviews(db: Session, model_id: int):
    return db.query(Review).filter(Review.shoe_model_id == model_id).all()


def get_review(db: Session, review_id: int):
    return db.query(Review).filter(Review.id == review_id).first()


def delete_model(db: Session, model_id: int):
    model = db.query(ShoeModel).filter(ShoeModel.id == model_id).first()
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")

    db.delete(model)
    db.commit()
