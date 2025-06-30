from fastapi import FastAPI
from api import review_routes
import os

app = FastAPI(title="Review Service", version="1.0.0")

os.makedirs("media", exist_ok=True)

app.include_router(review_routes.router, tags=["Reviews"])
