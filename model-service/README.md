# Model Service

Сервис управления моделями обуви (CRUD, хранение информации о моделях, фото и т.д.)

## Основные возможности
- Получение списка моделей
- Получение информации о модели
- Создание, обновление, удаление моделей (только для admin)

## Переменные окружения (пример .env.example)
```
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_db
POSTGRES_HOST=model-db
POSTGRES_PORT=5432
```

## Запуск

1. Скопируйте `.env.example` в `.env` и заполните переменные.
2. Соберите и запустите сервис через docker-compose:
   ```bash
   docker-compose up --build
   ```
3. Инициализируйте базу данных:
   ```bash
   docker-compose exec model-service python -m db.init_db
   ```

## Документация API
- Swagger: http://localhost:8000/docs

## Основные эндпоинты
| Метод   | Эндпоинт         | Назначение                        | Доступ         |
|---------|------------------|-----------------------------------|----------------|
| GET     | /models          | Получить список всех моделей      | Публичный      |
| GET     | /models/{id}     | Получить данные по одной модели   | Публичный      |
| POST    | /models          | Создать новую модель              | Только admin   |
| PATCH   | /models/{id}     | Обновить данные модели            | Только admin   |
| DELETE  | /models/{id}     | Удалить модель                    | Только admin   | 