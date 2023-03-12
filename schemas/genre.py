from pydantic import BaseModel
from typing import Optional


class Genre(BaseModel):

    id: Optional[int] = None
    name: str

    class Config:
        schema_extra = {
            "example": {
                "name": "name"
            }
        }
