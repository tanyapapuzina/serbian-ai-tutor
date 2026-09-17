from src.learning import LearningState
from src.tutor import TutorService


def test_create_activity_from_learning_state() -> None:
    service = TutorService()

    learning_state = LearningState(
        user_id="telegram:123",
        current_topic_id="latin_alphabet",
        current_topic_title="Serbian Latin alphabet",
    )

    activity = service.create_activity(learning_state)

    assert activity.topic_id == "latin_alphabet"
    assert activity.title == "Serbian Latin alphabet"
    assert "Serbian Latin alphabet" in activity.prompt