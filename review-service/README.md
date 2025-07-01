# Review Service

Сервис отзывов: добавление, редактирование, удаление отзывов пользователями и админами.

## Основные возможности
- Добавление отзыва к модели (только user)
- Редактирование и удаление своих отзывов (user)
- Удаление любых отзывов (admin)
- Получение списка всех отзывов (admin)

## Переменные окружения (пример .env.example)
```
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_db
POSTGRES_HOST=review-db
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
   docker-compose exec review-service python -m db.init_db
   ```

## Документация API
- Swagger: http://localhost:8001/docs

## Основные эндпоинты
| Метод   | Эндпоинт                 | Назначение                        | Доступ         |
|---------|--------------------------|-----------------------------------|----------------|
| POST    | /models/{id}/reviews     | Добавить отзыв и оценку           | Только user    |
| GET     | /reviews                 | Получить список всех отзывов      | Только admin   |
| PATCH   | /reviews/{id}            | Редактировать свой отзыв          | Только user    |
| DELETE  | /reviews/{id}            | Удалить свой или любой отзыв      | user/admin     | 