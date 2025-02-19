from uuid import UUID

from domain.contest_tasks.entities import ContestTask
from domain.contest_tasks.repositories import ContestTaskRepository
from application.transactions import TransactionsGateway


class ContestTaskReadUseCase:
    def __init__(self, repository: ContestTaskRepository, tx: TransactionsGateway):
        self.__repository = repository
        self.tx = tx

    async def __call__(self, uuid: UUID) -> ContestTask:
        return await self.__repository.read(uuid)
