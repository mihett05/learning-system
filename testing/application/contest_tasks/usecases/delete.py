from uuid import UUID

from application.contest_tasks.usecases import ReadContestTaskUseCase
from domain.contest_tasks.entities import ContestTask
from domain.contest_tasks.repositories import ContestTaskRepository

from application.transactions import TransactionsGateway


class DeleteContestTaskUseCase:
    def __init__(self, repository: ContestTaskRepository, tx: TransactionsGateway):
        self.__repository = repository
        self.__read_use_case = ReadContestTaskUseCase(self.__repository)
        self.transaction = tx

    async def __call__(self, uuid: UUID) -> ContestTask:
        async with self.transaction as transaction:
            entity = await self.__read_use_case(uuid)
            entity = await self.__repository.delete(entity)
            await transaction.commit()
            return entity
