from typing import Optional
from app.abstractions.register_chat_id_interface import IRegisterChatIDService
from app.abstractions.students_repo_interface import IStudentsRepository
import uuid


class RegisterChatIDService(IRegisterChatIDService):

    async def register_chat_id(self, repo: IStudentsRepository, chat_id: int, student_guid: Optional[str]) -> bool:
        try:
            if not student_guid:
                return False
            uuid.UUID(student_guid)
            student = await repo.find_free_guid(student_guid)
            if student:
                return False
            await repo.register_chatid(student_guid, chat_id)
            return True
        except ValueError:
            return False

