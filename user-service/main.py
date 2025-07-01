from fastapi import FastAPI
from api.user_routes import router as user_router

app = FastAPI(
    title="User Service",
    description="Сервис аутентификации и управления пользователями.",
    version="1.0",
)

app.include_router(user_router)


@app.get("/")
def root():
    return {"message": "User service is running"}
