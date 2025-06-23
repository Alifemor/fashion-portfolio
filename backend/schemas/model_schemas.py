from fastapi import UploadFile
from pydantic import BaseModel
from typing import List, Optional

class ShoeModelForm(BaseModel):
    name: str
    description: str
    tags: Optional[str] = None  
    photos: Optional[List[UploadFile]] = None

class ShoeModelCreate(ShoeModelBase):
    pass

class ShoeModelOut(ShoeModelBase):
    id: int
    created_at: datetime
    avg_rating: Optional[float]
    num_reviews: int

    class Config:
        orm_mode = True
