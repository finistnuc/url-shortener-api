# app/main.py
from fastapi import FastAPI
from app.api.endpoints import router  # Импортируем наш роутер

# Создаем экземпляр приложения FastAPI с метаданными
app = FastAPI(title="URL Shortener API", version="0.1.0")

# Подключаем роутер с эндпоинтами к нашему приложению
app.include_router(router)