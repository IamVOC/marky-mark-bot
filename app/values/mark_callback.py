from aiogram.filters.callback_data import CallbackData
from enum import Enum


class MarkEnum(Enum):
    G = 'G'
    R = 'R'
    Y = 'Y'
    B = 'B'

class MarkCallback(CallbackData, sep='|'):
    subject_id: int
    subject_date: str
    begin_lesson: str
    mark_type: MarkEnum

