from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.learning import StudySessionService

router = Router()


def build_user_id(message: Message) -> str:
    if message.from_user is None:
        return "telegram:unknown"

    return f"telegram:{message.from_user.id}"


def create_handlers(study_session_service: StudySessionService) -> Router:
    @router.message(CommandStart())
    async def handle_start(message: Message) -> None:
        user_id = build_user_id(message)
        activity = study_session_service.start_or_continue(user_id=user_id)

        await message.answer(activity.prompt)

    return router