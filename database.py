# database.py
# PostgreSQL connection for PgFinder

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession
)
from sqlalchemy.orm import (
    DeclarativeBase,
    sessionmaker
)

# Connection string
DATABASE_URL = (
    "postgresql+asyncpg://"
    "postgres:postgres@localhost/pgfinder"
)

# Create engine
engine = create_async_engine(
    DATABASE_URL,
    echo=True
)

# Create session
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


# Base class for models
class Base(DeclarativeBase):
    pass


# Dependency for FastAPI
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
