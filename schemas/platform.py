from pydantic import BaseModel
from typing import Optional


class Platform(BaseModel):

    id: Optional[int] = None
    name: str
    category: int

    class Config:
        schema_extra = {
            "example": {
                "name": "name",
                "category": 1
            }
        }
