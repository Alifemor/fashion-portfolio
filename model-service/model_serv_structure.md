# 🧠 Backend проекта Designer Portfolio

Этот каталог содержит backend-часть проекта на FastAPI.

## 📁 Структура папки

- `main.py` — точка входа, создаёт приложение FastAPI
- `api/` — маршруты API (роутеры)
  - `model_routes.py` — обработка моделей обуви
  - `review_routes.py` — добавление отзывов
- `crud/` — работа с базой (Create, Read, Update, Delete)
- `schemas/` — Pydantic-схемы (валидация входящих/исходящих данных)
- `models/` — SQLAlchemy-модели таблиц
- `core/` — конфигурация и настройки
  - `config.py` — ключи, URL-ы, базовые параметры
- `db/` — подключение к базе и Redis
  - `session.py` — SQLAlchemy-сессия
- `deps/` — зависимости, подключаемые через `Depends(...)`
- `.env` — переменные окружения (не коммитим в публичный репозиторий)
- `Dockerfile` — сборка контейнера
- `requirements.txt` — зависимости Python

## 🚀 Запуск локально

```bash
uvicorn main:app --reload
