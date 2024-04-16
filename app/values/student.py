from pydantic import BaseModel
from uuid import UUID


class StudentDTO(BaseModel):
    student_guid: UUID
    student_name: str
    chat_id: int
