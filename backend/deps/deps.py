from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
from backend.core.config import settings
from backend.db.session import SessionLocal

# Получение сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Проверка API-ключа (для админских маршрутов)
def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
