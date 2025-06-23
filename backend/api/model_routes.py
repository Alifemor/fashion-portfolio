from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List, Optional

from backend import crud
from backend.deps.deps import get_db

router = APIRouter()

@router.post("/models")
async def create_model(
    name: str = Form(...),
    description: str = Form(...),
    tags: Optional[str] = Form(None),
    photos: Optional[List[UploadFile]] = File(None),
    db: Session = Depends(get_db)
):
    # Обработка тегов
    tag_list = [tag.strip() for tag in tags.split(",")] if tags else []

    # Обработка фото
    photo_urls = []
    if photos:
        for photo in photos:
            contents = await photo.read()
            # сохранить в Redis и получить URL или ключ
            # временные ссылки по имени файла
            photo_urls.append(photo.filename)

    model_data = {
        "name": name,
        "description": description,
        "tags": tag_list,
        "photo_urls": photo_urls
    }

    return crud.create_model(db, model_data)
