# ⚙️ Backend (FastAPI)

Проектная логика backend'а реализована на FastAPI и взаимодействует с PostgreSQL и Redis.

---

## 📁 Структура проекта

```plaintext
backend/
├── main.py               # Точка входа
├── models/               # ORM-модели (Pydantic / SQLAlchemy)
├── schemas/              # Pydantic-схемы для валидации
├── crud/                 # Функции доступа к данным
├── api/                  # Роуты (endpoints)
├── deps/                 # Зависимости (например, проверка ключа)
├── core/                 # Конфигурации, utils
└── config.py             # Настройки проекта

