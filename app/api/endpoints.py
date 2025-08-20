# app/api/endpoints.py
from fastapi import APIRouter

# Добавляем префикс /hello и тег для документации
router = APIRouter(prefix="/hello", tags=["Greetings"])

@router.get("/")
async def read_root():
    return {"message": "Hello World"}

@router.get("/{name}")
async def read_hello(name: str):
    return {"message": f"Hello, {name}"}