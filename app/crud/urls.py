# app/crud/url.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import shortuuid

# Правильный импорт - из модуля url, а не из пакета schemas
from app.models.urls import URL
from app.schemas.urls import URLCreate  # <-- Вот так!

def generate_short_key() -> str:
    return shortuuid.uuid()[:8]

# CREATE - Создать новую запись в БД
async def create_db_url(db: AsyncSession, url: URLCreate) -> URL:
    # Генерируем уникальный ключ
    short_key = generate_short_key()
    # Создаем экземпляр модели SQLAlchemy
    db_url = URL(
        original_url=str(url.original_url),  # Преобразуем HttpUrl в строку
        short_key=short_key,
    )
    # Добавляем в сессию
    db.add(db_url)
    # Сохраняем изменения в БД
    await db.commit()
    # Обновляем наш объект данными из БД (например, чтобы получить id)
    await db.refresh(db_url)
    return db_url

# READ - Получить оригинальный URL по короткому ключу
async def get_db_url_by_key(db: AsyncSession, short_key: str) -> URL | None:
    # Строим асинхронный запрос к БД
    query = select(URL).where(URL.short_key == short_key)
    # Выполняем запрос и получаем результат
    result = await db.execute(query)
    # .scalar_one_or_none() вернет одну запись или None
    return result.scalar_one_or_none()