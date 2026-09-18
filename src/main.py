import asyncio

from src.bot import create_bot, create_dispatcher
from src.core import create_container, get_settings


async def main() -> None:
    settings = get_settings()
    container = create_container()

    bot = create_bot(token=settings.telegram_bot_token)
    dispatcher = create_dispatcher(container=container)

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())