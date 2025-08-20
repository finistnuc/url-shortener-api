# app/models/url.py
from sqlalchemy import Column, String, Integer, DateTime, func
from app.models.base import Base

class URL(Base):
    __tablename__ = "urls"  # Так будет называться таблица в БД

    # Атрибуты модели = колонки в таблице
    id = Column(Integer, primary_key=True, index=True)
    # original_url - длинная ссылка, которую нужно сократить
    original_url = Column(String, index=True, nullable=False)
    # short_key - короткий ключ (то, что будет в сокращенной ссылке)
    short_key = Column(String, unique=True, index=True, nullable=False)
    # created_at - время создания записи (проставится автоматически)
    created_at = Column(DateTime, server_default=func.now())

    # Строковое представление объекта (для отладки)
    def __repr__(self):
        return f"<URL(short_key='{self.short_key}', original_url='{self.original_url}')>"