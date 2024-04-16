import pytest
import pytest_asyncio
from sqlalchemy import insert

from app.db import async_session, engine
from app.models.base import Base
from app.models.student import Student
from app.values.student import StudentDTO
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
        students_query = insert(Student).values([{'student_guid': '720cc030-f2cc-4f31-8472-ee3a418270ac',
                                              'student_name': 'Dummy1', 'chat_id': 1},
                                             {'student_guid': '37e671c6-67b5-4077-83ed-93e621cd21d2',
                                              'student_name': 'Dummy2', 'chat_id': 2}
                                             ])
        await session.execute(students_query)
        repo = StudentsRepository(session)

        res = await repo.find_chatid(1)
    
    assert res == StudentDTO(student_guid='720cc030-f2cc-4f31-8472-ee3a418270ac',
                             student_name='Dummy1',
                             chat_id=1)

