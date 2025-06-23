from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# ======= ОТЗЫВЫ =======

class ReviewBase(BaseModel):
    name: str
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = None

class ReviewCreate(ReviewBase):
    pass

class ReviewOut(ReviewBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# ======= МОДЕЛИ ОБУВИ =======

class ShoeModelBase(BaseModel):
    name: str
    description: str
    photo_urls: List[str]
    tags: List[str]

class ShoeModelCreate(ShoeModelBase):
    pass

class ShoeModelOut(ShoeModelBase):
    id: int
    created_at: datetime
    avg_rating: Optional[float]
    num_reviews: int

    class Config:
        orm_mode = True

