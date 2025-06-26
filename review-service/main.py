from fastapi import FastAPI
from api import review_routes

app = FastAPI(title="Designer Portfolio API", version="1.0.0")

import os

# Создание директории для изображений (если отсутствует)
os.makedirs("media", exist_ok=True)

# Подключаем маршруты
app.include_router(review_routes.router, tags=["Reviews"])
