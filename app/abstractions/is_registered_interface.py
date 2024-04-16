from abc import ABC, abstractmethod

from app.abstractions.students_repo_interface import IStudentsRepository


class IIsRegisteredService(ABC):

    @abstractmethod
    async def is_registered(self, repo: IStudentsRepository, chat_id: int) -> bool:
        ...
