# User Service

Сервис аутентификации и управления пользователями для fashion-portfolio.

## Основные возможности
- Регистрация и вход по логину и паролю
- JWT-аутентификация
- Ограничение попыток входа (5 попыток, затем блокировка на 5 минут)
- 2 роли: user и admin
- Логирование входов, выходов, неудачных попыток

## Запуск

1. Убедитесь, что в корне проекта есть файл `.env` для user-service (или используйте дефолтные значения из примера).
2. Запустите проект через docker-compose:

```bash
docker-compose up --build
```

3. Сервис будет доступен на http://localhost:8002

## Инициализация базы данных

Для создания таблиц выполните:

```bash
docker-compose exec user-service python db/init_db.py
```

## Документация API

Swagger: http://localhost:8002/docs

## Пример .env

```
POSTGRES_USER=user_user
POSTGRES_PASSWORD=user_password
POSTGRES_DB=user_db
POSTGRES_HOST=user-db
POSTGRES_PORT=5432
JWT_SECRET=supersecretkey
JWT_ALGORITHM=HS256
``` 