from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend import crud, schemas
from backend.deps.deps import get_db

router = APIRouter()

@router.post("/models/{model_id}/reviews", response_model=schemas.ReviewOut)
def create_review(model_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    return crud.create_review(db, model_id, review)
