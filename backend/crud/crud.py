from sqlalchemy.orm import Session
from backend import models, schemas

# ======== МОДЕЛИ ОБУВИ ========

def get_models(db: Session):
    return db.query(models.ShoeModel).all()

def get_model(db: Session, model_id: int):
    return db.query(models.ShoeModel).filter(models.ShoeModel.id == model_id).first()

def create_model(db: Session, model: schemas.ShoeModelCreate):
    db_model = models.ShoeModel(**model.dict())
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model


# ======== ОТЗЫВЫ ========

def create_review(db: Session, model_id: int, review: schemas.ReviewCreate
