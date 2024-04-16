from abc import ABC, abstractmethod
from app.abstractions.students_repo_interface import IStudentsRepository


class IRegisterChatIDService(ABC):

    @abstractmethod
    async def register_chat_id(self, repo: IStudentsRepository, chat_id: int, student_guid: str) -> bool:
        ...
