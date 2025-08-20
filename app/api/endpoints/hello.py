# app/api/endpoints/hello.py
from fastapi import APIRouter

router = APIRouter(prefix="/hello", tags=["Greetings"])

@router.get("/")
async def read_root():
    return {"message": "Hello World"}

@router.get("/{name}")
async def read_hello(name: str):
    return {"message": f"Hello, {name}"}