from pydantic import BaseModel
from typing import Optional


class GameGenre(BaseModel):

    id: Optional[int] = None
    game_id: int
    genre_id: int

    class Config:
        schema_extra = {
            "example": {
                "game_id": 1,
                "genre_id": 1
            }
        }
