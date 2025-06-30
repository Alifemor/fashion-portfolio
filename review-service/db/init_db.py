import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.db_models import Base
from db.session import engine

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
