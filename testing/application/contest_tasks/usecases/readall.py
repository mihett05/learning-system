from uuid import UUID

from testing.domain.contest_tasks.entities import ContestTask
from testing.domain.contest_tasks.repositories import ContestTaskRepository


class ContestTaskReadAllUseCase:
    def __init__(self, repository: ContestTaskRepository):
        self.__repository = repository

    def __call__(self, uuids: list[UUID]) -> list[ContestTask]:
        return await self.__repository.read_all(uuids)
    
