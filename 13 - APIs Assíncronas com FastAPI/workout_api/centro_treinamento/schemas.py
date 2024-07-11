from typing import Annotated

from pydantic import Field
from contrib.schemas import BaseScehma


class CentroTreinamento(BaseScehma):
    nome: Annotated[str, Field(description="Nome do Centro de Treinamento", example="CT King", max_length=20)]
    endereço: Annotated[str, Field(description="Endereço do Centro de Treinamento", example="Avenida XXXXXXXXX", max_length=60)]
    proprietario: Annotated[str, Field(description="Proprietário do Centro de Treinamento", example="João Gomes", max_length=30)]
