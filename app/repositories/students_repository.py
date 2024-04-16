from typing import Optional
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.abstractions.students_repo_interface import IStudentsRepository
from app.values.student import StudentDTO
from app.models.student import Student


class StudentsRepository(IStudentsRepository):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def find_chatid(self, chat_id: int) -> Optional[StudentDTO]:
        stmt = (
                select(Student).
                where(Student.chat_id == chat_id)
        )
        rows = await self._session.execute(stmt)
        row = rows.one()
        if row:
            return StudentDTO.model_validate(row, from_attributes=True)

    async def find_free_guid(self, student_guid: str) -> Optional[StudentDTO]:
        stmt = (
                select(Student).
                where(Student.student_guid == student_guid).
                where(Student.chat_id == None)
        )
        rows = await self._session.execute(stmt)
        row = rows.one()
        if row:
            return StudentDTO.model_validate(row, from_attributes=True)


    async def register_chatid(self, student_guid: str, chat_id: int) -> None:
        stmt = (
                update(Student).
                where(Student.student_guid == student_guid).
                values(chat_id = chat_id)
        )
        await self._session.execute(stmt)
