from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class Game(BaseModel):

    id: Optional[int] = None
    name: str = Field(min_length=1)
    summary: str
    release_date: date
    category: int
    rating: float
    cover: str
    parent_id: int

    class Config:
        schema_extra = {
            "example": {
                "name": "example",
                "summary": "Summary example",
                "release_date": "2023-01-01",
                "category": 1,
                "rating": 1,
                "cover": "cover",
                "parent_id": 1
            }
        }
