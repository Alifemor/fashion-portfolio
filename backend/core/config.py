from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Designer Portfolio"
    API_KEY: str = "supersecretkey"  # поменяешь при необходимости
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/portfolio_db"
    REDIS_URL: str = "redis://localhost:6379"

    class Config:
        env_file = ".env"  # можно переопределить переменные через .env

settings = Settings()
