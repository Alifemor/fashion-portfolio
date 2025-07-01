import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
from fastapi import FastAPI
from api import model_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Designer Portfolio API", version="1.0.0")

import os

# Создание директории для изображений (если отсутствует)
os.makedirs("media", exist_ok=True)

# Подключаем маршруты
app.include_router(model_routes.router, tags=["Models"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Для продакшна укажите конкретный домен
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
