from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Subject(Base):
    __tablename__ = "subjects"

    subject_id: Mapped[int] = mapped_column(primary_key=True)
    subject_name: Mapped[str]
