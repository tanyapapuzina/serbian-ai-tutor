# models.py  — описывает структуру curriculum как Python-объекты

from pydantic import BaseModel, Field


class Topic(BaseModel): # одна тема
    id: str
    title: str


class Module(BaseModel): # раздел курса
    id: str
    title: str
    topics: list[Topic] = Field(default_factory=list)


class Curriculum(BaseModel): # весь YAML-файл целиком
    #BaseModel из Pydantic проверяет, что YAML имеет ожидаемую структуру

    version: str
    language: str
    learner_native_language: str
    level: str
    title: str
    modules: list[Module] = Field(default_factory=list)