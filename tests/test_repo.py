import pytest
import pytest_asyncio

from app.db import async_session, engine
from app.models.base import Base
from app.repositories.students_repository import StudentsRepository

@pytest_asyncio.fixture
async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.mark.asyncio
async def test_succesful_find_by_chat_id(setup_db):
    async with async_session() as session:
        repo = StudentsRepository(session)

        res = await repo.find_chatid(1)
    
    assert res == None

