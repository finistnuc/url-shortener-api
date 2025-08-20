# app/main.py
from fastapi import FastAPI
# ЗДЕСЬ ИСПРАВЛЕНИЕ: импортируем router напрямую из модулей
from app.api.endpoints.hello import router as hello_router
from app.api.endpoints.urls import router as urls_router
from app.models.base import Base
from app.database import engine

app = FastAPI(title="URL Shortener API", version="0.1.0")

# Подключаем оба роутера
app.include_router(hello_router)
app.include_router(urls_router)

@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)