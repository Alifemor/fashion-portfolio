from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from core.config import settings
from crud import operations as crud
from schemas import review_schemas
from deps.deps import get_db
from uuid import UUID
from shared.jwt_auth import get_current_user, TokenData
from models.db_models import Review
from sqlalchemy import func


# Заглушка для get_current_user (реализовать через shared или прямой импорт)
class User:
    id: UUID
    role: str


def get_current_user():
    # TODO: реализовать получение пользователя через JWT
    raise NotImplementedError


router = APIRouter()


@router.get("/models/{model_id}/reviews", response_model=list[review_schemas.ReviewOut])
def get_reviews_by_model(model_id: int, db: Session = Depends(get_db)):
    return crud.get_reviews(db, model_id)


@router.get("/reviews", response_model=list[review_schemas.ReviewOut])
def read_all_reviews(db: Session = Depends(get_db)):
    return crud.get_all_reviews(db)


@router.post("/models/{model_id}/reviews", response_model=review_schemas.ReviewOut)
def create_review(
    model_id: int,
    review: review_schemas.ReviewCreate,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    return crud.create_review(db, model_id, review, user_id=current_user.sub)


@router.put("/reviews/{review_id}", response_model=review_schemas.ReviewOut)
def update_review(
    review_id: int,
    updated_review: review_schemas.ReviewCreate,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    db_review = crud.get_review(db, review_id)
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")
    if str(db_review.user_id) != current_user.sub and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Нет прав на редактирование")
    return crud.update_review(db, review_id, updated_review)


@router.patch("/reviews/{review_id}", response_model=review_schemas.ReviewOut)
def update_review_partial(
    review_id: int,
    review_data: review_schemas.ReviewUpdate,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    db_review = crud.get_review(db, review_id)
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")
    if str(db_review.user_id) != current_user.sub and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Нет прав на редактирование")
    return crud.update_review_partial(db, review_id, review_data)


@router.delete("/reviews/{review_id}", status_code=204)
def delete_review(
    review_id: int,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
):
    db_review = crud.get_review(db, review_id)
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")
    if str(db_review.user_id) != current_user.sub and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Нет прав на удаление")
    crud.delete_review(db, review_id)
    return Response(status_code=204)


@router.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}


@router.get("/stats", tags=["Stats"])
def stats(db: Session = Depends(get_db)):
    total = db.query(Review).count()
    avg_rating = db.query(func.avg(Review.rating)).scalar() or 0
    return {"reviews": total, "avg_rating": round(avg_rating, 2)}
