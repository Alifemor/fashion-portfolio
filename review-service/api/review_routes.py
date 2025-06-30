from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from core.config import settings

from crud import operations as crud
from schemas import review_schemas
from deps.deps import get_db

router = APIRouter()


@router.get("/reviews", response_model=list[review_schemas.ReviewOut])
def read_all_reviews(db: Session = Depends(get_db)):
    return crud.get_all_reviews(db)


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


@router.patch("/reviews/{review_id}", response_model=review_schemas.ReviewOut)
def update_review_partial(
    review_id: int,
    review_data: review_schemas.ReviewUpdate,
    db: Session = Depends(get_db),
    x_api_key: str = Header(...),
):
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden")
    review = crud.update_review_partial(db, review_id, review_data)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review


@router.delete("/reviews/{review_id}", status_code=204)
def delete_review(
    review_id: int,
    db: Session = Depends(get_db),
    x_api_key: str = Header(..., alias="x-api-key"),
):
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    crud.delete_review(db, review_id)
    return Response(status_code=204)
