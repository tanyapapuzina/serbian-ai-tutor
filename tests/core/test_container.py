from src.core import create_container


def test_create_container_builds_study_session_service() -> None:
    container = create_container()

    activity = container.study_session_service.start_or_continue(
        user_id="telegram:123",
    )

    assert activity.topic_id == "latin_alphabet"
    assert activity.title == "Serbian Latin alphabet"