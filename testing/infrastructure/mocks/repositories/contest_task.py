from uuid import UUID

from domain.contest_tasks.dtos import CreateContestTaskDto
from domain.contest_tasks.entities import ContestTask
from domain.contest_tasks.repositories import ContestTaskRepository
from domain.contest_tasks.exceptions import (
    ContestTaskAlreadyExistsException,
    ContestTasksNotFoundException,
)

from .crud import MockRepository, MockRepositoryConfig, Id


class ContestTaskMemoryRepository(ContestTaskRepository):
    class Config(MockRepositoryConfig):
        def __init__(self):
            super().__init__(
                entity=ContestTask,
                not_found_exception=ContestTasksNotFoundException,
                already_exists_exception=ContestTaskAlreadyExistsException,
            )

        def extract_id(self, entity: ContestTask) -> Id:
            return entity.task_info_id

    def __init__(self):
        self.__repository = MockRepository(self.Config())

    async def create(self, create_dto: CreateContestTaskDto) -> ContestTask:
        return await self.__repository.create(
            ContestTask(
                task_info_id=create_dto.task_info_id,
                time_limit=create_dto.time_limit,
                memory_limit=create_dto.memory_limit,
                execution_tests=[],
            )
        )

    async def read(self, uuid: UUID) -> ContestTask:
        return await self.__repository.read(uuid)

    async def read_all(self, uuids: list[UUID]) -> list[ContestTask]:
        return [await self.__repository.read(uuid) for uuid in uuids]

    async def update(self, task: ContestTask) -> ContestTask:
        return await self.__repository.update(task)

    async def delete(self, task: ContestTask) -> ContestTask:
        return await self.__repository.delete(task)
