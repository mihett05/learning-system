from uuid import UUID

from testing.application.contest_tasks.usecases import ContestTaskReadUseCase
from testing.domain.contest_tasks.entities import ContestTask
from testing.domain.contest_tasks.repositories import ContestTaskRepository


class ContestTaskDeleteUseCase:
    def __init__(self, repository: ContestTaskRepository):
        self.__repository = repository

    def __call__(self, uuid: UUID) -> ContestTask:
        entity = ContestTaskReadUseCase(self.__repository).__call__(uuid)
        return await self.__repository.delete(entity)
