from models.base import Base
from db.session import engine
import models.db_models  # noqa: F401


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
