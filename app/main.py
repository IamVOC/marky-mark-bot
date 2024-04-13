from aiogram import Dispatcher, Bot
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp.web import Application, run_app

from app.routes.start_route import start_router
from app.config import get_settings


async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(f"{get_settings().WEBHOOK_HOST}{get_settings().WEBHOOK_PATH}")

def main() -> None:
    config = get_settings() 
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.startup.register(on_startup)
    bot = Bot(config.TOKEN)
    app = Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot
    )
    webhook_requests_handler.register(app, path=config.WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    run_app(app, host=config.WEB_SERVER_HOST, port=config.WEB_SERVER_PORT)


if __name__ == "__main__":
    main()
