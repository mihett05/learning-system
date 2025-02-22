from domain.execution_tests.dtos import CreateExecutionTestDto
from domain.execution_tests.repositories import ExecutionTestRepository
from domain.execution_tests.entities import ExecutionTest


class CreateContestTaskUseCase:
    def __init__(self, repository: ExecutionTestRepository):
        self.__repository = repository

    async def __call__(self, dto: CreateExecutionTestDto) -> ExecutionTest:
        return await self.__repository.create(dto)
