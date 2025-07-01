import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
from fastapi import FastAPI
from api import review_routes
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Review Service", version="1.0.0")

os.makedirs("media", exist_ok=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Для продакшна укажите конкретный домен
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(review_routes.router, tags=["Reviews"])
