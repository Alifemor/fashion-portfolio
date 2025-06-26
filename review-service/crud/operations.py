# crud/operations.py
from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.db_models import Review
import schemas
from core.config import settings
import redis

# Подключение к Redis
r = redis.Redis.from_url(settings.redis_url, decode_responses=True)


def create_review(db: Session, model_id: int, review: schemas.ReviewCreate):
    db_review = Review(**review.dict(), shoe_model_id=model_id)
    db.add(db_review)

    # ⚠️ TODO: уведомить модельный сервис об изменении рейтинга (например, через API или очередь)
    # пример: requests.post("http://model-service:8000/internal/recalculate-rating", json={...})

    db.commit()
    db.refresh(db_review)
    return db_review


def get_reviews(db: Session, model_id: int):
    return db.query(Review).filter(Review.shoe_model_id == model_id).all()


def get_all_reviews(db: Session):
    return db.query(Review).all()


def get_review(db: Session, review_id: int):
    return db.query(Review).filter(Review.id == review_id).first()


def update_review(
    db: Session, model_id: int, review_id: int, updated_review: schemas.ReviewCreate
):
    review = (
        db.query(Review)
        .filter(Review.id == review_id, Review.shoe_model_id == model_id)
        .first()
    )

    if not review:
        return None

    review.name = updated_review.name
    review.rating = updated_review.rating
    review.comment = updated_review.comment

    db.commit()
    db.refresh(review)
    return review


def update_review_partial(
    db: Session, review_id: int, review_data: schemas.ReviewUpdate
):
    db_review = db.query(Review).filter(Review.id == review_id).first()
    if not db_review:
        return None

    for field, value in review_data.dict(exclude_unset=True).items():
        setattr(db_review, field, value)

    db.commit()
    db.refresh(db_review)
    return db_review


def delete_review(db: Session, review_id: int):
    review = db.query(Review).filter(Review.id == review_id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    db.delete(review)
    db.commit()
