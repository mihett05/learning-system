from uuid import UUID

from fastapi import APIRouter
from dishka.integrations.fastapi import DishkaRoute, FromDishka

from application.contest_tasks.usecases import ContestTaskReadUseCase
from infrastructure.http.api.models import ErrorModel

from .models import ContestTaskModel
from .mappers import map_to_pydantic


router = APIRouter(route_class=DishkaRoute, tags=["Contest tasks"])


@router.get(
    "/{uuid}", response_model=ContestTaskModel, responses={404: {"model": ErrorModel}}
)
async def get_contest_task(uuid: UUID, use_case: FromDishka[ContestTaskReadUseCase]):
    return map_to_pydantic(await use_case(uuid))
