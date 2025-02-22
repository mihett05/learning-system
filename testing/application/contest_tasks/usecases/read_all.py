from uuid import UUID

from domain.contest_tasks.entities import ContestTask
from domain.contest_tasks.repositories import ContestTaskRepository


class ReadAllContestTaskUseCase:
    def __init__(self, repository: ContestTaskRepository):
        self.__repository = repository

    async def __call__(self, uuids: list[UUID]) -> list[ContestTask]:
        return await self.__repository.read_all(uuids)
