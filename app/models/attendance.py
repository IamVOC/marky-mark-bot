from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, Enum
from sqlalchemy import ForeignKey
import enum

from .base import Base


class VisitEnum(enum.Enum):
    VISITED = 'visited'
    SKIPPED = 'skipped'
    SKIPPED_WITH_REASON = 'skipped_with_reason'
    OTHER_GROUP = 'other_group'

class Attendance(Base):
    __tablename__ = "attendance"

    attendance_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    student_guid: Mapped[str] = mapped_column(ForeignKey('students.student_guid'))
    subject_id: Mapped[int] = mapped_column(ForeignKey('subjects.subject_id'))
    date: Mapped[str] = mapped_column(DateTime)
    visit: Mapped[str] = mapped_column(Enum(VisitEnum))
