from pydantic import BaseModel


class BaseScehma(BaseModel):
    class Config:
        extra = "forbid"
        from_attributes = True
