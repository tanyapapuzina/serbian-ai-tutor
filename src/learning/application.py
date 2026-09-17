from src.learning.service import LearningService
from src.tutor import LearningActivity, TutorService


class StudySessionService:
    def __init__(
        self,
        learning_service: LearningService,
        tutor_service: TutorService,
    ) -> None:
        self.learning_service = learning_service
        self.tutor_service = tutor_service

    def start_or_continue(self, user_id: str) -> LearningActivity:
        learning_state = self.learning_service.start_or_continue(user_id=user_id)
        return self.tutor_service.create_activity(learning_state=learning_state)