from dataclasses import dataclass
from pathlib import Path

from src.curriculum import CurriculumRepository
from src.learning import LearningService, StudySessionService
from src.tutor import TutorService


@dataclass(frozen=True)
class Container:
    curriculum_repository: CurriculumRepository
    learning_service: LearningService
    tutor_service: TutorService
    study_session_service: StudySessionService


def create_container(
    curriculum_path: Path = Path("curriculum/a1/curriculum.yaml"),
) -> Container:
    curriculum_repository = CurriculumRepository.from_yaml(curriculum_path)
    learning_service = LearningService(curriculum=curriculum_repository)
    tutor_service = TutorService()
    study_session_service = StudySessionService(
        learning_service=learning_service,
        tutor_service=tutor_service,
    )

    return Container(
        curriculum_repository=curriculum_repository,
        learning_service=learning_service,
        tutor_service=tutor_service,
        study_session_service=study_session_service,
    )