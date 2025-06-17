import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config.config import Config, load_config

# Import the routers
# Current imports handlers
from handlers import user_handlers, other_handlers

# Import supporrting functions for creating require objects

# Initalize logger
logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )
    # Stdout about starting launch the bot
    logger.info("Starting bot")

    # Load config to config var
    config: Config = load_config()

    # Initalize storage object
    storage = None

    # Initalize bot and dispathcer

    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher(storage=storage)

    # Initalize another objects (db, cache ant etc.)

    # Put require objects in dispathcer`s workflow_data
    # dp.workflow_data.update(objects)

    # Register the routers
    logger.info("Connect the routers")

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Register middleware
    logger.info("Connect the middleware")
    # ...

    # Missing collect update and start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
