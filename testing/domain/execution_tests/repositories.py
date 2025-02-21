from abc import ABCMeta, abstractmethod
from uuid import UUID

from .dtos import CreateExecutionTestDto, ReadExecutionTestDto
from .entities import ExecutionTest

class ExecutionTestRepository(metaclass=ABCMeta):
    @abstractmethod
    async def create(self, create_dto: CreateExecutionTestDto) -> ExecutionTest: ...
    @abstractmethod
    async def read(self, uuid: UUID) -> ExecutionTest: ...
    @abstractmethod
    async def read_all(self, dto: ReadExecutionTestDto) -> list[ExecutionTest]: ...
    @abstractmethod
    async def delete(self, test: ExecutionTest) -> ExecutionTest: ...
