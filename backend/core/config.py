from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Designer Portfolio"
    API_KEY: str = "supersecretkey"
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/portfolio_db"
    REDIS_URL: str = "redis://localhost:6379"
    DEBUG: bool = True  
    
    class Config:
        env_file = ".env"

settings = Settings()
