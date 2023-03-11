from pydantic import BaseModel, Field
from typing import Optional


class Critic(BaseModel):

    id: Optional[int] = None
    title: str = Field(min_length=1)
    body: str
    user_id: int
    company_id: int
    game_id: int

    class Config:
        schema_extra = {
            "example": {
                "title": "Title",
                "body": "Body critic",
                "user_id": 0,
                "company_id": 0,
                "game_id": 0
            }
        }
