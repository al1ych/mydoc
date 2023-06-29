from pydantic import BaseModel, Field


class UserModel(BaseModel):
    id: int = Field(..., example=39459192)
    name: str
