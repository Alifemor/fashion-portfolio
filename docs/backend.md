# ⚙️ Backend (FastAPI)

Проектная логика backend'а реализована на FastAPI и взаимодействует с PostgreSQL и Redis.

---

## 📁 Структура проекта

```plaintext
backend/
├── main.py               # Точка входа в FastAPI-приложение
├── api/                  # Маршруты API (роутеры)
│   ├── model_routes.py   # Работа с моделями
│   └── review_routes.py  # Работа с отзывами
├── models/               # SQLAlchemy-модели таблиц
├── schemas/              # Pydantic-схемы запроса/ответа
├── crud/                 # Логика взаимодействия с БД
├── deps/                 # Зависимости через Depends (например, API-ключ)
├── db/                   # Подключения к PostgreSQL и Redis
│   └── session.py        # SQLAlchemy-сессия
├── core/
│   └── config.py         # Настройки проекта
├── .env                  # Переменные окружения
├── Dockerfile            # Docker-сборка backend-сервиса
└── requirements.txt      # Python-зависимости


