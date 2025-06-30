from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from models.base import Base


class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True, index=True)
    shoe_model_id = Column(Integer, nullable=False)  # удалён ForeignKey
    name = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
