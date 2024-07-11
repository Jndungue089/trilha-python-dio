from uuid import uuid4
from fastapi import APIRouter, status, Body
from contrib.dependencies import DatabaseDependency
from categorias.schemas import CategoriaIn, CategoriaOut
from categorias.models import CategoriaModel

router = APIRouter()

@router.post(
    path='/',
    summary='Criar nova categoria',
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut
)
async def post(db_session: DatabaseDependency, categoria_in: CategoriaIn = Body(...)) -> CategoriaOut:
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dumo())
    breakpoint()
    pass
