# app/api/endpoints.py
from fastapi import APIRouter  # <-- Импортируем роутер

# Создаем экземпляр роутера. Префикс и теги можно будет добавить позже.
router = APIRouter()

# Заменяем @app.get на @router.get
@router.get("/")
async def read_root():
    return {"message": "Hello World"}

@router.get("/{name}")
async def read_hello(name: str):
    return {"message": f"Hello, {name}"}