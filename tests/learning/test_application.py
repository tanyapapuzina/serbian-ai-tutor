from pathlib import Path

from src.curriculum import CurriculumRepository
from src.learning import LearningService, StudySessionService
from src.tutor import TutorService

CURRICULUM_PATH = Path("curriculum/a1/curriculum.yaml")


def test_study_session_start_or_continue_returns_activity() -> None:
    curriculum = CurriculumRepository.from_yaml(CURRICULUM_PATH)
    learning_service = LearningService(curriculum=curriculum)
    tutor_service = TutorService()
    study_service = StudySessionService(
        learning_service=learning_service,
        tutor_service=tutor_service,
    )

    activity = study_service.start_or_continue(user_id="telegram:123")

    assert activity.topic_id == "latin_alphabet"
    assert activity.title == "Serbian Latin alphabet"
    assert "Serbian Latin alphabet" in activity.prompt