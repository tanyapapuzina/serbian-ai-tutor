from pydantic import BaseModel


class LearningActivity(BaseModel):
    topic_id: str
    title: str
    prompt: str