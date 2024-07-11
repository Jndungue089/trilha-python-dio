from typing import Annotated
from pydantic import BaseModel, UUID4, Field
from datetime import datetime


class BaseScehma(BaseModel):
    class Config:
        extra = "forbid"
        from_attributes = True


class OutMixin(BaseScehma):
    id: Annotated[UUID4, Field(description='Identificador')]
    created_at: Annotated[datetime, Field(description='Data de Criação')]
