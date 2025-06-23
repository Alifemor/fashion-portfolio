from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend import crud, schemas
from backend.deps.deps import get_db

router = APIRouter()

@router.get("/models", response_model=list[schemas.ShoeModelOut])
def list_models(db: Session = Depends(get_db)):
    return crud.get_models(db)


@router.get("/models/{model_id}", response_model=schemas.ShoeModelOut)
def get_model(model_id: int, db: Session = Depends(get_db)):
    model = crud.get_model(db, model_id)
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")
    return model


@router.post("/models", response_model=schemas.ShoeModelOut)
def create_model(model: schemas.ShoeModelCreate, db: Session = Depends(get_db)):
    return crud.create_model(db, model)

