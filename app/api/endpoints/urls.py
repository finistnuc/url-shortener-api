# app/api/endpoints/urls.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

# ИМПОРТИРУЕМ НАПРЯМУЮ ИЗ ФАЙЛА, А НЕ ИЗ ПАКЕТА
from app.schemas.urls import URL, URLCreate  # <-- Вот так правильно!
from app.crud.urls import create_db_url, get_db_url_by_key
from app.database import get_db

router = APIRouter(prefix="/urls", tags=["urls"])

# Теперь response_model=URL будет работать
@router.post("/", response_model=URL)
async def create_url(url: URLCreate, db: AsyncSession = Depends(get_db)):
    db_url = await create_db_url(db=db, url=url)
    return db_url

@router.get("/{key}", response_model=URL)
async def get_url_info(key: str, db: AsyncSession = Depends(get_db)):
    db_url = await get_db_url_by_key(db=db, short_key=key)
    if db_url is None:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return db_url