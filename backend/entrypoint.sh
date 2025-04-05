#!/bin/bash

# Загружаем переменные окружения из .env
export $(grep -v '^#' .env | xargs)

if [[ "$DEBUGPY" == "1" ]]; then
    echo "Запуск сервера с debugpy. Ожидание подключения..."
    exec python -m debugpy --listen 0.0.0.0:5678 --wait-for-client manage.py runserver 0.0.0.0:8000 --nothreading --noreload
else
    echo "Запуск в обычном режиме..."
    exec python manage.py runserver 0.0.0.0:8000
fi