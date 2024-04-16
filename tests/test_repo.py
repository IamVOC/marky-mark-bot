import pytest
from sqlalchemy.exc import NoResultFound

from app.db import async_session
from app.values.student import StudentDTO
from app.repositories.students_repository import StudentsRepository


@pytest.mark.asyncio
async def test_succesful_find_by_chat_id():
    async with async_session() as session:
        repo = StudentsRepository(session)

        res = await repo.find_chatid(1)
    
    assert res == StudentDTO(student_guid='720cc030-f2cc-4f31-8472-ee3a418270ac',
                             student_name='Dummy1',
                             chat_id=1)

@pytest.mark.asyncio
async def test_failed_find_by_chat_id():
    async with async_session() as session:
        repo = StudentsRepository(session)
        try:
            res = await repo.find_chatid(2)
            assert False
        except NoResultFound:
            assert True



