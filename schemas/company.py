from pydantic import BaseModel, Field
from datetime import date
from typing import Optional


class Company(BaseModel):

    id: Optional[int] = None
    name: str = Field(min_length=1)
    description: str
    start_date: date
    country: str
    cover: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Name",
                "description": "Company Description",
                "start_date": "2023-01-01",
                "country": "Peru",
                "cover": "Cover"
            }
        }
