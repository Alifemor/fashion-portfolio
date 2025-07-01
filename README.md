# 👠 Designer Portfolio Showcase

Микросервисный веб-проект для публикации моделей обуви, отзывов пользователей и сбора аналитики по интересу к дизайнам.

## 🏗️ Архитектура

Проект состоит из следующих микросервисов:

- **user-service** — аутентификация, регистрация, роли, JWT, логирование
- **model-service** — управление моделями обуви
- **review-service** — отзывы пользователей и админов
- **Redis** — кэширование фото

Подробнее: [docs/architecture.md](docs/architecture.md)

## 🚀 Запуск

1. Скопируйте `.env.example` в `.env` для каждого сервиса и заполните переменные.
2. Запустите проект:
   ```bash
   docker-compose up --build
   ```
3. Инициализируйте базы данных (пример для user-service):
   ```bash
   docker-compose exec user-service python -m db.init_db
   ```

## 📚 Документация сервисов

- [User Service README](user-service/README.md) | [Swagger](http://localhost:8002/docs)
- [Model Service README](model-service/README.md) | [Swagger](http://localhost:8000/docs)
- [Review Service README](review-service/README.md) | [Swagger](http://localhost:8001/docs)

## 🗂️ Полезные ссылки

- [Цели и контекст проекта](docs/business-goals.md)
- [Пользовательские сценарии](docs/User_Story/user-stories.md)
- [Структура базы данных](docs/database/DB_README.md)
- [API-маршруты и структура](docs/API/API_README.md)
- [Архитектура проекта](docs/architecture.md)

## 🏷️ Статус

- В разработке. Ведётся развитие микросервисной архитектуры.

## 🧪 Тесты

В каждом микросервисе есть папка `tests/` с базовыми тестами (pytest + FastAPI TestClient).

### Как запустить тесты

1. Перейдите в папку нужного сервиса, например:
   ```bash
   cd user-service
   ```
2. Запустите тесты:
   ```bash
   pytest
   ```

Тесты позволяют убедиться, что основные сценарии работают корректно и сервисы готовы к интеграции с фронтендом.
