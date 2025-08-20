# app/main.py
from fastapi import FastAPI
from app.api.endpoints import router
from app.models.base import Base
from app.database import engine

app = FastAPI(title="URL Shortener API", version="0.1.0")

# Подключаем роутер
app.include_router(router)

# Событие на запуск приложения: создает таблицы в БД
@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)  # Раскомментируйте, чтобы сбросить все таблицы!
        await conn.run_sync(Base.metadata.create_all)  # Создает все таблицы из наших моделей