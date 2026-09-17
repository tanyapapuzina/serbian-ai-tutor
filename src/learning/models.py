from pydantic import BaseModel


class LearningState(BaseModel):
    user_id: str
    current_topic_id: str
    current_topic_title: str