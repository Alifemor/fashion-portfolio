# User Service

Сервис аутентификации и управления пользователями для fashion-portfolio.

## Основные возможности
- Регистрация и вход по логину и паролю
- JWT-аутентификация
- Ограничение попыток входа (5 попыток, затем блокировка на 5 минут)
- 2 роли: user и admin
- Логирование входов, выходов, неудачных попыток

## Запуск

1. Скопируйте `.env.example` в `.env` и заполните переменные.
2. Запустите проект через docker-compose:

```bash
docker-compose up --build
```

3. Сервис будет доступен на http://localhost:8002

## Инициализация базы данных

Для создания таблиц выполните:

```bash
docker-compose exec user-service python -m db.init_db
```

## Документация API

Swagger: http://localhost:8002/docs

## Пример .env.example
```
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_db
POSTGRES_HOST=user-db
POSTGRES_PORT=5432
JWT_SECRET=your_jwt_secret
JWT_ALGORITHM=HS256
``` 