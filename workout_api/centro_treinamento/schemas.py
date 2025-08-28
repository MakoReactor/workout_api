from typing import Annotated
from pydantic import Field
from workout_api.contrib.schemas import BaseSchema

class ControleTreinamento(BaseSchema):
    nome: Annotated(
        [str, Field(description="Nome do centro de treinamento", examples="Centro 01", max_length=20)]
    )
    endereco: Annotated(
        [str, Field(description="Endereço", examples="Rua 5 nº 127", max_length=100)]
    )
    proprietario: Annotated(
        [str, Field(description="Nome do proprietário", examples="Cesar", max_length=30)]
    )