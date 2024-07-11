from fastapi import APIRouter, status, Body
from contrib.dependencies import DatabaseDependency
from atleta.schemas import AtletaIn

router = APIRouter()


@router.post(
    path='/',
    summary='Criar novo atleta',
    status_code=status.HTTP_201_CREATED
)
async def post(db_session: DatabaseDependency, atleta_in: AtletaIn = Body(...)):
    pass