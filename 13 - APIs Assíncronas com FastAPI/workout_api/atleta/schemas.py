from pydantic import Field, PositiveFloat
from typing import Annotated
from contrib.schemas import BaseScehma, OutMixin

class Atleta(BaseScehma):
    nome: Annotated[str, Field(description="Nome do atleta",
                               examples=["João"],  # Change to list
                               max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta",
                              examples=["12345678901"],  # Change to list
                              max_length=11)]
    idade: Annotated[int, Field(description="idade do atleta",
                                examples=[25])]  # Change to list
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta",
                                         examples=[69.5])]  # Change to list
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta (em m)",
                                           examples=[1.70])]  # Change to list
    sexo: Annotated[str, Field(description="Sexo do atleta",
                               examples=["M/F"],  # Change to list
                               max_length=1)]


class AtletaIn(Atleta):
    pass


class AtletaOut(AtletaIn, OutMixin):
    pass
