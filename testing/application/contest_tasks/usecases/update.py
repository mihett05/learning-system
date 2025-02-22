from testing.application.contest_tasks.usecases import ContestTaskReadUseCase
from testing.domain.contest_tasks.dtos import UpdateContestTaskDto
from testing.domain.contest_tasks.entities import ContestTask
from testing.domain.contest_tasks.repositories import ContestTaskRepository


class ContestTaskUpdateUseCase:
    def __init__(self, repository: ContestTaskRepository):
        self.__repository = repository

    def __call__(self, dto: UpdateContestTaskDto) -> ContestTask:
        entity = ContestTaskReadUseCase(self.__repository).__call__(dto.task_info_id)
        entity.time_limit = dto.time_limit
        entity.memory_limit = dto.memory_limit
        return await self.__repository.update(entity)
