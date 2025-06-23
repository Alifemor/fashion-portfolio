from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from uuid import uuid4
import os

from backend import crud, schemas
from backend.deps.deps import get_db

router = APIRouter()

MEDIA_DIR = "media"
os.makedirs(MEDIA_DIR, exist_ok=True)

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
def create_model(
    name: str = Depends(),
    description: str = Depends(),
    tags: str = Depends(),
    files: list[UploadFile] = File(...),
    db: Session = Depends(get_db)
):
    filenames = []
    for file in files:
        ext = os.path.splitext(file.filename)[1]
        filename = f"{uuid4().hex}{ext}"
        filepath = os.path.join(MEDIA_DIR, filename)
        with open(filepath, "wb") as buffer:
            buffer.write(file.file.read())
        filenames.append(filepath)

    model_in = schemas.ShoeModelCreate(
        name=name,
        description=description,
        tags=tags.split(","),
        photo_urls=filenames
    )
    return crud.create_model(db, model_in)
