# 🧑‍💻 Архитектура проекта

## Микросервисная структура

Проект реализован в виде набора микросервисов, каждый из которых отвечает за свою бизнес-логику и имеет отдельную базу данных (PostgreSQL):

- **user-service** — сервис аутентификации, регистрации, управления пользователями и ролями (user/admin), JWT-авторизация, логирование входов/выходов/ошибок.
- **model-service** — сервис управления моделями обуви (CRUD, хранение информации о моделях, фото и т.д.).
- **review-service** — сервис отзывов: добавление, редактирование, удаление отзывов пользователями и админами.

Вспомогательные сервисы:
- **Redis** — кэширование фото моделей.

## Взаимодействие сервисов

- Все сервисы общаются через REST API.
- Для доступа к защищённым эндпоинтам используется JWT (выдаётся user-service).
- Каждый сервис имеет свою документацию (Swagger/OpenAPI).

## Схема взаимодействия

```mermaid
graph TD;
  User((Пользователь))
  user-service[User Service]
  model-service[Model Service]
  review-service[Review Service]
  redis[Redis]
  db1[(User DB)]
  db2[(Model DB)]
  db3[(Review DB)]

  User-->|REST/JWT|user-service
  User-->|REST/JWT|model-service
  User-->|REST/JWT|review-service
  user-service-->|PostgreSQL|db1
  model-service-->|PostgreSQL|db2
  review-service-->|PostgreSQL|db3
  model-service-->|Redis|redis
```

## Документация сервисов

- [User Service README](../../user-service/README.md)
- [Model Service README](../../model-service/README.md)
- [Review Service README](../../review-service/README.md)

## Развёртывание

Проект разворачивается через `docker-compose` (см. корневой README). Каждый сервис запускается в отдельном контейнере.

