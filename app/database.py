# app/database.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# Формат строки подключения:
# postgresql+asyncpg://<username>:<password>@<host>/<database_name>
# Пока используем значения по умолчанию. Мы настроим реальную БД позже через Docker.
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/url_shortener_db"

# Движок — это точка входа в БД, которая управляет подключениями.
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,  # Выводит все SQL-запросы в консоль (очень полезно для отладки!)
    future=True # Включаем поддержку нового API SQLAlchemy 2.0
)

# SessionLocal — это фабрика для создания асинхронных сессий.
# Сессия — это основной объект, через который происходят все операции с БД.
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)

# Функция-зависимость (Dependency) для получения сессии в эндпоинтах FastAPI.
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()  # Фиксируем изменения, если не было ошибок
        except Exception:
            await session.rollback() # Откатываем изменения в случае ошибки
            raise
        finally:
            await session.close()