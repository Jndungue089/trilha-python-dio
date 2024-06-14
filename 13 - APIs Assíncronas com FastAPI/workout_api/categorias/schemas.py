from typing import Annotated

from pydantic import Field
from workout_api.contrib.schemas import BaseScehma


class Categorias(BaseScehma):
    nome: Annotated[str, Field(description="Nome da Categoria", examples="Scale", max_length=10)]
