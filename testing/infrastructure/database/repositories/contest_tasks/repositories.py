from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.orm.interfaces import LoaderOption

from domain.contest_tasks.dtos import CreateContestTaskDto
from domain.contest_tasks.entities import ContestTask
from domain.contest_tasks.repositories import ContestTaskRepository
from domain.contest_tasks.exceptions import (
    ContestTaskAlreadyExistsException,
    ContestTasksNotFoundException,
)

from .models import ContestTaskDbModel
from .mappers import map_to_db, map_from_db, map_create_db
from ..repository import PostgresRepositoryConfig, PostgresRepository, Id


class ContestTaskDatabaseRepository(ContestTaskRepository):
    class Config(PostgresRepositoryConfig):
        def __init__(self):
            super().__init__(
                model=ContestTaskDbModel,
                entity=ContestTask,
                entity_mapper=map_from_db,
                model_mapper=map_to_db,
                create_mapper=map_create_db,
                not_found_exception=ContestTasksNotFoundException,
                already_exists_exception=ContestTaskAlreadyExistsException,
            )

        def extract_id_from_entity(self, entity: ContestTask) -> Id:
            return entity.task_info_id

        def extract_id_from_model(self, model: ContestTaskDbModel) -> Id:
            return model.task_info_id

        def get_options(self) -> list[LoaderOption]:
            return [selectinload(ContestTaskDbModel.execution_tests)]

    def __init__(self, session: AsyncSession):
        self.__session = session
        self.__repository = PostgresRepository(session, self.Config())

    async def create(self, create_dto: CreateContestTaskDto) -> ContestTask:
        return await self.__repository.create(create_dto)

    async def read(self, uuid: UUID) -> ContestTask:
        return await self.__repository.read(uuid)

    async def read_all(self, uuids: list[UUID]) -> list[ContestTask]:
        return await self.__repository.get_entities_from_query(
            select(ContestTaskDbModel).where(ContestTaskDbModel.task_info_id.in_(uuids))
        )

    async def update(self, task: ContestTask) -> ContestTask:
        return await self.__repository.update(task)

    async def delete(self, task: ContestTask) -> ContestTask:
        return await self.__repository.delete(task)
