from uuid import UUID

from domain.execution_tests.repositories import ExecutionTestRepository
from domain.execution_tests.entities import ExecutionTest


class ReadExecutionTestUseCase:
    def __init__(self, repository: ExecutionTestRepository):
        self.__repository = repository

    async def __call__(self, uuid: UUID) -> ExecutionTest:
        return await self.__repository.read(uuid)
