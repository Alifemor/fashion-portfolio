import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    JWT_SECRET = os.getenv("JWT_SECRET", "supersecretkey")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = 60
    MAX_LOGIN_ATTEMPTS = 5
    LOGIN_BLOCK_TIME_MINUTES = 5


settings = Settings()
