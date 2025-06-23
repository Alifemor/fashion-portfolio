FROM python:3.11-slim

# Создаём рабочую директорию
WORKDIR /app

# Копируем зависимости и устанавливаем
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY . .

# Указываем команду запуска
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
