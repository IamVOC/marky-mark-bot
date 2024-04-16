from aiogram import Router
from aiogram.types import CallbackQuery

from app.values.mark_callback import MarkCallback


mark_route = Router()

@mark_route.callback_query()
async def mark_query(query: CallbackQuery, callback_data: MarkCallback):
    ...
