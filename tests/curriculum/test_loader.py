from pathlib import Path

import pytest

from src.curriculum import CurriculumRepository

CURRICULUM_PATH = Path("curriculum/a1/curriculum.yaml")


def test_loads_curriculum_from_yaml() -> None:
    curriculum = CurriculumRepository.from_yaml(CURRICULUM_PATH)

    assert curriculum.curriculum.level == "A1"
    assert curriculum.curriculum.language == "sr"
    assert curriculum.curriculum.learner_native_language == "ru"


def test_get_first_topic() -> None:
    curriculum = CurriculumRepository.from_yaml(CURRICULUM_PATH)

    first_topic = curriculum.get_first_topic()

    assert first_topic.id == "latin_alphabet"
    assert first_topic.title == "Serbian Latin alphabet"


def test_get_topic_by_id() -> None:
    curriculum = CurriculumRepository.from_yaml(CURRICULUM_PATH)

    topic = curriculum.get_topic("accusative_direction")

    assert topic.id == "accusative_direction"
    assert topic.title == "Direction: u/na + accusative"


def test_get_next_topic() -> None:
    curriculum = CurriculumRepository.from_yaml(CURRICULUM_PATH)

    next_topic = curriculum.get_next_topic("accusative_direction")

    assert next_topic is not None
    assert next_topic.id == "locative_intro"


def test_get_next_topic_returns_none_for_last_topic() -> None:
    curriculum = CurriculumRepository.from_yaml(CURRICULUM_PATH)

    next_topic = curriculum.get_next_topic("final_assessment")

    assert next_topic is None


def test_unknown_topic_raises_error() -> None:
    curriculum = CurriculumRepository.from_yaml(CURRICULUM_PATH)

    with pytest.raises(ValueError, match="Unknown topic"):
        curriculum.get_topic("unknown_topic")