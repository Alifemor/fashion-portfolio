from models.db_models import Base
from db.session import engine

def init_db():
    Base.metadata.create_all(bind=engine)