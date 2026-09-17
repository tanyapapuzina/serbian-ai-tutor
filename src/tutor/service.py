from src.learning.models import LearningState
from src.tutor.models import LearningActivity


class TutorService:
    def create_activity(self, learning_state: LearningState) -> LearningActivity:
        return LearningActivity(
            topic_id=learning_state.current_topic_id,
            title=learning_state.current_topic_title,
            prompt=(
                f"Текущая тема: {learning_state.current_topic_title}.\n\n"
                "Начнём с короткого объяснения и простого упражнения."
            ),
        )