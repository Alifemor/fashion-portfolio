# api/model_routes.py

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
import os, uuid
from backend import crud, schemas
from backend.deps.deps import get_db
from backend.core.config import settings
import redis

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
    db: Session = Depends(get_db)
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
        name=name,
        description=description,
        tags=[t.strip() for t in tags.split(",")]
    )

    return crud.create_model(db, model_data, photo_urls=saved_paths)
