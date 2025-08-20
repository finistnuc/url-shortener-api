# app/schemas/urls.py
from pydantic import BaseModel, HttpUrl
from datetime import datetime

# Базовая схема для атрибутов, общих для нескольких операций
class URLBase(BaseModel):
    original_url: HttpUrl  # Pydantic сам проверит, что это валидный URL

# Схема для создания новой ссылки (то, что ожидает POST-запрос)
class URLCreate(URLBase):
    pass  # Пока что нам не нужно ничего, кроме original_url

# Схема для ответа API (то, что мы возвращаем пользователю)
class URL(URLBase):
    short_key: str
    created_at: datetime

    # Эта настройка позволяет ORM работать с SQLAlchemy-моделями
    class Config:
        from_attributes = True  # Работает вместо старого orm_mode = True