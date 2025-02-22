from domain.contest_tasks.dtos import CreateContestTaskDto
from domain.contest_tasks.entities import ContestTask
from domain.contest_tasks.repositories import ContestTaskRepository


class CreateContestTaskUseCase:
    def __init__(self, repository: ContestTaskRepository):
        self.__repository = repository

    async def __call__(self, dto: CreateContestTaskDto) -> ContestTask:
        return await self.__repository.create(dto)
