from src.curriculum import CurriculumRepository
from src.learning.models import LearningState


class LearningService:
    def __init__(self, curriculum: CurriculumRepository) -> None:
        self.curriculum = curriculum

    def start_or_continue(self, user_id: str) -> LearningState:
        current_topic = self.curriculum.get_first_topic()

        return LearningState(
            user_id=user_id,
            current_topic_id=current_topic.id,
            current_topic_title=current_topic.title,
        )