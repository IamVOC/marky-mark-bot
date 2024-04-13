from pydantic import BaseModel


class StudentDTO(BaseModel):
    student_guid: str
    student_name: str
    chat_id: int
