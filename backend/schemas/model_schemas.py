from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

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
