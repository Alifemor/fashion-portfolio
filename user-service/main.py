from fastapi import FastAPI
from api.user_routes import router as user_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="User Service",
    description="Сервис аутентификации и управления пользователями.",
    version="1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Для продакшна укажите конкретный домен
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)


@app.get("/")
def root():
    return {"message": "User service is running"}
