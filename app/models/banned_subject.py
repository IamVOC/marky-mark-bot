from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from .base import Base


class BannedSubject(Base):
    __tablename__ = 'banned_subjects'

    subject_id: Mapped[int] = mapped_column(ForeignKey('subjects.subject_id'), primary_key=True)
