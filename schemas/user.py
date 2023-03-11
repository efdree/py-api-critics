from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):

    id: Optional[int] = None
    username: str = Field(min_length=1)
    email: str = Field(
        min_length=5, regex="([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
    password: str = Field(min_length=6)
    role: str
    critics_count = Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "username": "example",
                "email": "example@mail.com",
                "password": "******",
                "role": "admin",
                "critics_count": 0
            }
        }
