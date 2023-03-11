from pydantic import BaseModel
from typing import Optional


class GamePlatform(BaseModel):

    id: Optional[int] = None
    game_id: int
    platform_id: int

    class Config:
        schema_extra = {
            "example": {
                "game_id": 1,
                "platform_id": 1
            }
        }
