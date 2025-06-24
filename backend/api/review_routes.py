from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from core.config import settings

from crud import operations as crud
from schemas import review_schemas
from deps.deps import get_db

router = APIRouter()


@router.post("/models/{model_id}/reviews", response_model=review_schemas.ReviewOut)
def create_review(
    model_id: int, review: review_schemas.ReviewCreate, db: Session = Depends(get_db)
):
    return crud.create_review(db, model_id, review)


@router.get("/models/{model_id}/reviews", response_model=list[review_schemas.ReviewOut])
def get_reviews(model_id: int, db: Session = Depends(get_db)):
    return crud.get_reviews(db, model_id)


from fastapi import Header


@router.put(
    "/reviews/{review_id}",
    response_model=review_schemas.ReviewOut,
    dependencies=[Depends(get_db)],
)
def update_review(
    review_id: int,
    updated_review: review_schemas.ReviewCreate,
    db: Session = Depends(get_db),
    x_api_key: str = Header(...),
):
    # Временная проверка API-ключа
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    db_review = crud.get_review(db, review_id)
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")

    db_review.name = updated_review.name
    db_review.rating = updated_review.rating
    db_review.comment = updated_review.comment
    db.commit()
    db.refresh(db_review)
    return db_review
