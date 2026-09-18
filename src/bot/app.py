from aiogram import Bot, Dispatcher

from src.bot.handlers import create_handlers
from src.core import Container


def create_dispatcher(container: Container) -> Dispatcher:
    dispatcher = Dispatcher()
    dispatcher.include_router(
        create_handlers(
            study_session_service=container.study_session_service,
        )
    )
    return dispatcher


def create_bot(token: str) -> Bot:
    return Bot(token=token)