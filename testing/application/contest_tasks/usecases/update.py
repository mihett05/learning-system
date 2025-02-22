from application.contest_tasks.usecases import ReadContestTaskUseCase
from domain.contest_tasks.dtos import UpdateContestTaskDto
from domain.contest_tasks.entities import ContestTask
from domain.contest_tasks.repositories import ContestTaskRepository

from application.transactions import TransactionsGateway


class UpdateContestTaskUseCase:
    def __init__(self, repository: ContestTaskRepository, tx: TransactionsGateway, uc: ReadContestTaskUseCase):
        self.__repository = repository
        self.__read_use_case = uc
        self.transaction = tx

    async def __call__(self, dto: UpdateContestTaskDto) -> ContestTask:
        async with self.transaction as transaction:
            entity = await self.__read_use_case(dto.task_info_id)
            entity.time_limit = dto.time_limit
            entity.memory_limit = dto.memory_limit
            entity = await self.__repository.update(entity)
            await transaction.commit()
            return entity
