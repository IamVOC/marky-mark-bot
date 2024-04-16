from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.fsm import Menu
from app.services.is_registered_service import IsRegisteredService
from app.services.register_chat_id_service import RegisterChatIDService
from app.repositories.students_repository import StudentsRepository
from app.db import async_session
from app.constants import START_MESSAGE, REGISTERED_MESSAGE, SUCCESSFUL_MESSAGE


start_router = Router()

@start_router.message(CommandStart())
async def check_register(message: Message, state: FSMContext) -> None:
    async with async_session() as session:
        repo = StudentsRepository(session)
        service = IsRegisteredService()
        is_registered = await service.is_registered(repo=repo, chat_id=message.chat.id)
    if is_registered:
        await state.set_state(Menu.schedule)
    else:
        await state.set_state(Menu.register)
        await message.answer(START_MESSAGE)

@start_router.message(Menu.register)
async def register_student(message: Message, state: FSMContext) -> None:
    async with async_session() as session:
        repo = StudentsRepository(session)
        service = RegisterChatIDService()
        is_not_registered = await service.register_chat_id(repo=repo, chat_id=message.chat.id, student_guid=message.text)
    if is_not_registered:
        await state.set_state(Menu.schedule)
        await message.answer(SUCCESSFUL_MESSAGE)
    else:
        await message.answer(REGISTERED_MESSAGE)

