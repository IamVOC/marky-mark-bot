import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import engine
from app.models.base import Base


@pytest_asyncio.fixture
async def eng():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        yield
        await conn.run_sync(Base.metadata.drop_all)

@pytest_asyncio.fixture
async def session(eng):
    async with AsyncSession(eng) as session:
        yield session
