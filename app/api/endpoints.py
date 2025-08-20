from fastapi import APIRouter  # <-- Новый импорт!
from app.main import app       # Импортируем экземпляр app

# Создаем роутер вместо того, чтобы использовать app напрямую
router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Hello World"}

@router.get("/{name}")
async def read_hello(name: str):
    return {"message": f"Hello, {name}"}