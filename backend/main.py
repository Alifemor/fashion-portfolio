from fastapi import FastAPI
from backend.api import model_routes, review_routes

app = FastAPI(
    title="Designer Portfolio API",
    version="1.0.0"
)

# Подключаем маршруты
app.include_router(model_routes.router, tags=["Models"])
app.include_router(review_routes.router, tags=["Reviews"])
