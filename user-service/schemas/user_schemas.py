from pydantic import BaseModel, constr
from typing import Optional
from uuid import UUID
from enum import Enum
from datetime import datetime


class UserRole(str, Enum):
    user = "user"
    admin = "admin"


class UserCreate(BaseModel):
    login: constr(min_length=3, max_length=32)
    password: constr(min_length=6, max_length=128)
    display_name: constr(min_length=1, max_length=64)


class UserLogin(BaseModel):
    login: str
    password: str


class UserOut(BaseModel):
    id: UUID
    login: str
    display_name: str
    role: UserRole


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserLogOut(BaseModel):
    id: int
    user_id: Optional[UUID]
    action: str
    timestamp: datetime
    ip: Optional[str]
