from aiogram.fsm.state import StatesGroup, State


class Menu(StatesGroup):
    register = State()
    schedule = State()

