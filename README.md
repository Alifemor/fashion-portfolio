#  Designer Portfolio Showcase

Микросервисный веб-проект для публикации моделей обуви, отзывов пользователей и сбора аналитики по интересу к дизайнам.

##  Архитектура

Проект состоит из следующих микросервисов:

- **user-service** — аутентификация, регистрация, роли, JWT, логирование
- **model-service** — управление моделями обуви
- **review-service** — отзывы пользователей и админов
- **Redis** — кэширование фото

Подробнее: [docs/architecture.md](docs/architecture.md)

##  Запуск

1. Скопируйте `.env.example` в `.env` для каждого сервиса и заполните переменные.
2. Запустите проект:
   ```bash
   docker-compose up --build
   ```
3. Инициализируйте базы данных (пример для user-service):
   ```bash
   docker-compose exec user-service python -m db.init_db
   ```

##  Документация сервисов

- [User Service README](user-service/README.md) | [Swagger](http://localhost:8002/docs)
- [Model Service README](model-service/README.md) | [Swagger](http://localhost:8000/docs)
- [Review Service README](review-service/README.md) | [Swagger](http://localhost:8001/docs)

##  Полезные ссылки

- [Цели и контекст проекта](docs/business-goals.md)
- [Пользовательские сценарии](docs/User_Story/user-stories.md)
- [Структура базы данных](docs/database/DB_README.md)
- [API-маршруты и структура](docs/API/API_README.md)
- [Архитектура проекта](docs/architecture.md)

##  Статус

- В разработке. Ведётся разработка фронтенда.

##  Тесты

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

##  Минимальная отчётность и мониторинг

В каждом сервисе реализованы специальные эндпоинты:

- `/health` — проверка доступности сервиса (healthcheck для мониторинга и оркестрации).
- `/stats` — минимальная статистика по сервису:
    - **user-service**: количество пользователей и админов
    - **model-service**: количество моделей
    - **review-service**: количество отзывов и средний рейтинг

Пример запроса:
```bash
curl http://localhost:8002/health
curl http://localhost:8002/stats
```

##  Примеры запросов для фронтенда

### Регистрация пользователя
POST /register
```json
{
  "login": "user1",
  "password": "password123",
  "display_name": "User One"
}
```

### Вход (получение JWT)
POST /login
```json
{
  "login": "user1",
  "password": "password123"
}
```
Ответ:
```json
{
  "access_token": "jwt...",
  "token_type": "bearer"
}
```

### Создание отзыва (нужен JWT)
POST /models/{model_id}/reviews
Заголовок: Authorization: Bearer <jwt>
```json
{
  "rating": 5,
  "comment": "Отличная модель!"
}
```

## Интеграция с фронтендом

### Генерация клиента из OpenAPI

Для TypeScript/JS:
```bash
npx openapi-typescript-codegen --input user-service/openapi.json --output src/api/user
npx openapi-typescript-codegen --input model-service/openapi.json --output src/api/model
npx openapi-typescript-codegen --input review-service/openapi.json --output src/api/review
```

### Авторизация

- После логина сохраняйте access_token (JWT) в localStorage/sessionStorage.
- Для всех защищённых запросов добавляйте заголовок:
  ```
  Authorization: Bearer <ваш_JWT>
  ```

### Пример запроса с JWT (fetch)

```js
fetch('http://localhost:8002/me', {
  headers: {
    'Authorization': 'Bearer ' + localStorage.getItem('access_token')
  }
})
  .then(res => res.json())
  .then(data => console.log(data));
```

## Переменные окружения и безопасность

- Для каждого сервиса есть файл `.env.example` — скопируйте его в `.env` и заполните своими значениями для локального запуска.
- Никогда не используйте реальные секреты и пароли из продакшн-версии в публичном репозитории!
- Для релиза на боевом сервере используйте отдельные значения переменных окружения (секреты, пароли, имена БД и т.д.).
