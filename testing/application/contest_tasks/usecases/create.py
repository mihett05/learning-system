from testing.domain.contest_tasks.dtos import CreateContestTaskDto
from testing.domain.contest_tasks.entities import ContestTask
from testing.domain.contest_tasks.repositories import ContestTaskRepository


class ContestTaskCreateUseCase:
    def __init__(self, repository: ContestTaskRepository):
        self.__repository = repository

    def __call__(self, dto: CreateContestTaskDto) -> ContestTask:
        return await self.__repository.create(dto)
