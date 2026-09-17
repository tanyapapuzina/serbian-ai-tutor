# loader.py  — читает YAML и даёт удобные методы навигации

# CurriculumRepository загружает эту структуру из YAML,
# валидирует её и предоставляет Learning Engine удобный 
# интерфейс навигации по программе обучения

from pathlib import Path

import yaml

from src.curriculum.models import Curriculum, Module, Topic


class CurriculumRepository:
    def __init__(self, curriculum: Curriculum) -> None:
        self.curriculum = curriculum
        self._topics = self._build_topic_index() # словарь для быстрого поиска темы по id:
        self._topic_order = self._build_topic_order() # список всех тем по порядку

    @classmethod # создает новый объект класса
    def from_yaml(cls, path: Path) -> "CurriculumRepository":
        with path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        curriculum = Curriculum.model_validate(data)
        return cls(curriculum)

    def get_first_topic(self) -> Topic:
        if not self._topic_order:
            raise ValueError("Curriculum has no topics")

        return self._topic_order[0]

    def get_topic(self, topic_id: str) -> Topic:
        try:
            return self._topics[topic_id]
        except KeyError as exc:
            raise ValueError(f"Unknown topic: {topic_id}") from exc

    def get_next_topic(self, topic_id: str) -> Topic | None:
        for index, topic in enumerate(self._topic_order):
            if topic.id == topic_id:
                next_index = index + 1
                if next_index >= len(self._topic_order):
                    return None
                return self._topic_order[next_index]

        raise ValueError(f"Unknown topic: {topic_id}")

    def get_module_for_topic(self, topic_id: str) -> Module:
        for module in self.curriculum.modules:
            for topic in module.topics:
                if topic.id == topic_id:
                    return module

        raise ValueError(f"Unknown topic: {topic_id}")

    def _build_topic_index(self) -> dict[str, Topic]: # поиск по ID
        topics: dict[str, Topic] = {}

        for module in self.curriculum.modules:
            for topic in module.topics:
                if topic.id in topics:
                    raise ValueError(f"Duplicate topic id: {topic.id}")

                topics[topic.id] = topic

        return topics

    def _build_topic_order(self) -> list[Topic]: # сохраняет последовательность тем 
        return [
            topic
            for module in self.curriculum.modules
            for topic in module.topics
        ]