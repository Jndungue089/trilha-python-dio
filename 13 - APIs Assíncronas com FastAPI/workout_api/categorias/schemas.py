from typing import Annotated

from pydantic import Field, UUID4
from contrib.schemas import BaseScehma


class Categorias(BaseScehma):
    nome: Annotated[str, Field(description="Nome da Categoria", examples=["Scale"], max_length=10)]
    

class CategoriaIn(Categorias):
    pass


class CategoriaOut(Categorias):
    id: Annotated[UUID4, Field(description="Identificador da categoria")]