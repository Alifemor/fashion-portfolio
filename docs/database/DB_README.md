## 🗂️ Структура базы данных (актуальная)

### Таблицы

#### users (user-service)
- id (uuid, PK)
- login (уникальный логин)
- password_hash (хэш пароля)
- display_name (отображаемое имя)
- role (user/admin)
- failed_login_attempts (счётчик неудачных попыток)
- last_failed_login (время последней неудачной попытки)

#### user_logs (user-service)
- id (PK)
- user_id (uuid, FK на users.id)
- action (login, logout, failed_login)
- timestamp (дата/время)
- ip (IP-адрес)

#### shoe_model (model-service)
- id (PK)
- name (название модели)
- description (описание)
- photo_urls (массив ссылок на фото)
- tags (массив тегов)
- created_at (дата создания)
- avg_rating (средний рейтинг)
- num_reviews (количество отзывов)

#### review (review-service)
- id (PK)
- shoe_model_id (FK на shoe_model.id)
- name (имя пользователя)
- rating (оценка)
- comment (текст отзыва)
- created_at (дата создания)

### Связи
- Один пользователь может иметь много логов (users.id → user_logs.user_id)
- Одна модель может иметь много отзывов (shoe_model.id → review.shoe_model_id)

### ER-диаграмма
- [ER-диаграмма (PNG)](./ERD.png)
- [Исходник схемы (DBML)](./schema.dbml)

