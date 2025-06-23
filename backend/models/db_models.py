from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, ARRAY
from sqlalchemy.orm import relationship
from datetime import datetime

from models.base import Base  # уже без backend

class ShoeModel(Base):
    __tablename__ = "shoe_model"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    photo_urls = Column(ARRAY(String))
    tags = Column(ARRAY(String))
    created_at = Column(DateTime, default=datetime.utcnow)
    avg_rating = Column(Float, default=0.0)
    num_reviews = Column(Integer, default=0)

    reviews = relationship("Review", back_populates="shoe_model")


class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True, index=True)
    shoe_model_id = Column(Integer, ForeignKey("shoe_model.id", ondelete="CASCADE"))
    name = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    shoe_model = relationship("ShoeModel", back_populates="reviews")
