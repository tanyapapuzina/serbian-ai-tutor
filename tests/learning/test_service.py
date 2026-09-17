from pathlib import Path

from src.curriculum import CurriculumRepository
from src.learning import LearningService

CURRICULUM_PATH = Path("curriculum/a1/curriculum.yaml")


def test_start_or_continue_returns_first_topic_for_new_user() -> None:
    curriculum = CurriculumRepository.from_yaml(CURRICULUM_PATH)
    service = LearningService(curriculum=curriculum)

    state = service.start_or_continue(user_id="telegram:123")

    assert state.user_id == "telegram:123"
    assert state.current_topic_id == "latin_alphabet"
    assert state.current_topic_title == "Serbian Latin alphabet"