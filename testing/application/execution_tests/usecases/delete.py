from uuid import UUID

from application.execution_tests.usecases import ReadExecutionTestUseCase
from application.transactions import TransactionsGateway

from domain.execution_tests.repositories import ExecutionTestRepository
from domain.execution_tests.entities import ExecutionTest


class DeleteExecutionTestUseCase:
    def __init__(self, repository: ExecutionTestRepository, transaction: TransactionsGateway, read_use_case: ReadExecutionTestUseCase):
        self.__repository = repository
        self.__read_use_case = read_use_case
        self.__transaction = transaction

    async def __call__(self, uuid: UUID) -> ExecutionTest:
        async with self.__transaction as transaction:
            entity = await self.__read_use_case(uuid)
            entity = await self.__repository.delete(entity)
            await transaction.commit()
            return entity
