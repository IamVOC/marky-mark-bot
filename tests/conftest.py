import pytest_asyncio
from sqlalchemy import insert

from app.db import engine, async_session
from app.models.base import Base
from app.models.student import Student


@pytest_asyncio.fixture(scope='module', autouse=True)
async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    async with async_session() as session:
        students_query = insert(Student).values([{'student_guid': '720cc030-f2cc-4f31-8472-ee3a418270ac',
                                              'student_name': 'Dummy1', 'chat_id': 1},
                                             {'student_guid': '37e671c6-67b5-4077-83ed-93e621cd21d2',
                                              'student_name': 'Dummy2'}
                                             ])
        await session.execute(students_query)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

