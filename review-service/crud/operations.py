from sqlalchemy.orm import Session
from models.db_models import Review
import schemas.review_schemas as schemas
from core.config import settings
import redis
from fastapi import HTTPException


r = redis.Redis.from_url(settings.redis_url, decode_responses=True)


def create_review(db: Session, model_id: int, review: schemas.ReviewCreate, user_id):
    db_review = Review(
        shoe_model_id=model_id,
        user_id=user_id,
        rating=review.rating,
        comment=review.comment,
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def get_reviews(db: Session, model_id: int):
    return db.query(Review).filter(Review.shoe_model_id == model_id).all()


def get_all_reviews(db: Session):
    return db.query(Review).all()


def get_review(db: Session, review_id: int):
    return db.query(Review).filter(Review.id == review_id).first()


def update_review(db: Session, review_id: int, updated_review: schemas.ReviewCreate):
    review = db.query(Review).filter(Review.id == review_id).first()
    if not review:
        return None
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
    for field, value in review_data.model_dump(exclude_unset=True).items():
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
