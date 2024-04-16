from app.abstractions.is_registered_interface import IIsRegisteredService
from app.abstractions.students_repo_interface import IStudentsRepository


class IsRegisteredService(IIsRegisteredService):

    async def is_registered(self, repo: IStudentsRepository, chat_id: int) -> bool:
        student = await repo.find_chatid(chat_id)
        if student:
            return True
        return False

