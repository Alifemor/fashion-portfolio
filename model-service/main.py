from fastapi import FastAPI
from api import model_routes

app = FastAPI(title="Designer Portfolio API", version="1.0.0")

import os

# Создание директории для изображений (если отсутствует)
os.makedirs("media", exist_ok=True)

# Подключаем маршруты
app.include_router(model_routes.router, tags=["Models"])

