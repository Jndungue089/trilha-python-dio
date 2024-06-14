from pydantic import Field, PositiveFloat
from typing import Annotated
from workout_api.contrib.schemas import BaseScehma


class Atleta(BaseScehma):
    nome: Annotated(str, Field(description="Nome do atleta",
                               examples="João",
                               max_length=50))
    cpf: Annotated(str, Field(description="CPF do atleta",
                               examples="12345678901",
                               max_length=11))
    idade: Annotated(int, Field(description="idade do atleta",
                               examples=25))
    peso: Annotated(PositiveFloat, Field(description="Peso do atleta",
                                examples=69.5))  # type: ignore
    altura: Annotated(PositiveFloat, Field(description="Altura do atleta (em m)",
                               examples=1.70))
    sexo: Annotated(str, Field(description="Sexo do atleta",
                               examples="M/F",
                               max_length=1))