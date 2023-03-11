from pydantic import BaseModel
from typing import Optional


class Genre(BaseModel):

    id: Optional[int] = None
    name: str
    genregame_id: int

    class Config:
        schema_extra = {
            "example": {
                "name": "name",
                "genregame_id": 1
            }
        }
