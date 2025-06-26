from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from datetime import datetime
from models.base import Base

class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True, index=True)
    shoe_model_id = Column(Integer, ForeignKey("shoe_model.id", ondelete="CASCADE"))
    name = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

