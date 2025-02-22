from uuid import UUID

from domain.contest_tasks.entities import ContestTask
from domain.contest_tasks.repositories import ContestTaskRepository


class ContestTaskReadUseCase:
    def __init__(self, repository: ContestTaskRepository): #Gateway лишний, использовался Мишей во время тестов
        self.__repository = repository

    async def __call__(self, uuid: UUID) -> ContestTask:
        return await self.__repository.read(uuid)
