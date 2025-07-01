# api/model_routes.py
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
import os, uuid

from crud import operations as crud
from schemas import model_schemas as schemas
from deps.deps import get_db, verify_api_key
from core.config import settings
import redis
from models.db_models import ShoeModel


router = APIRouter()

r = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)

MEDIA_DIR = "media"
os.makedirs(MEDIA_DIR, exist_ok=True)


@router.post("/models", response_model=schemas.ShoeModelOut)
async def create_model(
    name: str = Form(...),
    description: str = Form(...),
    tags: str = Form(...),  # передаём список тегов одной строкой через запятую
    photos: list[UploadFile] = File(...),
    db: Session = Depends(get_db),
):
    saved_paths = []

    for photo in photos:
        ext = os.path.splitext(photo.filename)[1]
        filename = f"{uuid.uuid4().hex}{ext}"
        file_path = os.path.join(MEDIA_DIR, filename)

        with open(file_path, "wb") as buffer:
            buffer.write(await photo.read())

        redis_key = f"photo:{filename}"
        r.set(redis_key, file_path)  # путь к файлу сохраняем в Redis
        saved_paths.append(file_path)

    model_data = schemas.ShoeModelCreate(
        name=name, description=description, tags=[t.strip() for t in tags.split(",")]
    )

    return crud.create_model(db, model_data, photo_urls=saved_paths)


@router.get("/models", response_model=list[schemas.ShoeModelOut])
def list_models(db: Session = Depends(get_db)):
    return crud.get_models(db)


@router.get("/models/{model_id}", response_model=schemas.ShoeModelOut)
def get_model(model_id: int, db: Session = Depends(get_db)):
    model = crud.get_model(db, model_id)
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")
    return model


@router.delete("/models/{model_id}", status_code=204)
def delete_model(
    model_id: int,
    db: Session = Depends(get_db),
    x_api_key: str = Depends(verify_api_key),
):
    crud.delete_model(db, model_id)
    return


@router.put(
    "/models/{model_id}",
    response_model=schemas.ShoeModelOut,
    dependencies=[Depends(verify_api_key)],
)
def update_model(
    model_id: int,
    model: schemas.ShoeModelCreate,
    db: Session = Depends(get_db),
):
    db_model = crud.get_model(db, model_id)
    if not db_model:
        raise HTTPException(status_code=404, detail="Model not found")

    db_model.name = model.name
    db_model.description = model.description
    db_model.tags = model.tags
    db_model.photo_urls = model.photo_urls

    db.commit()
    db.refresh(db_model)
    return db_model


@router.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}


@router.get("/stats", tags=["Stats"])
def stats(db: Session = Depends(get_db)):
    total = db.query(ShoeModel).count()
    return {"models": total}
