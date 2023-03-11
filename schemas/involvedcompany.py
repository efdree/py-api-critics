from pydantic import BaseModel, Field
from typing import Optional


class InvolvedCompany(BaseModel):

    id: Optional[int] = None
    developer: Optional[bool] = False
    publisher: Optional[bool] = False
    company_id: int
    game_id: int

    class Config:
        schema_extra = {
            "example": {
                "developer": False,
                "publisher": False,
                "company_id": 0,
                "game_id": 0
            }
        }
