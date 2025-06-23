# schemas/model_schemas.py

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# ======= МОДЕЛИ ОБУВИ =======

class ShoeModelBase(BaseModel):
    name: str
    description: str
    tags: List[str]

class ShoeModelCreate(ShoeModelBase):
    pass  # больше не ожидаем photo_urls

class ShoeModelOut(ShoeModelBase):
    id: int
    created_at: datetime
    avg_rating: Optional[float]
    num_reviews: int
    photo_urls: List[str]

    class Config:
        orm_mode = True
