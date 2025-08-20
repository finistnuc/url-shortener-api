from fastapi import FastAPI

app = FastAPI(title="URL Shortener API", version="0.1.0")

# Это будет подключено позже
from app.api.endpoints import router
app.include_router(router)