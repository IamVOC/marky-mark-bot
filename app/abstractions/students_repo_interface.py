from abc import ABC, abstractmethod
from typing import Optional

from app.values.student import StudentDTO


class IStudentsRepository(ABC):

    @abstractmethod
    async def find_chatid(self, chat_id: int) -> Optional[StudentDTO]:
        ...

    @abstractmethod
    async def find_free_guid(self, student_guid: str) -> Optional[StudentDTO]:
        ...

    @abstractmethod
    async def register_chatid(self, student_guid: str, chat_id: int) -> None:
        ...
