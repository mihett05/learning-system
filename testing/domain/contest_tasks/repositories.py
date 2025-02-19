from abc import ABCMeta, abstractmethod
from uuid import UUID

from .dtos import CreateContestTaskDto
from .entities import ContestTask


class ContestTaskRepository(metaclass=ABCMeta):
    @abstractmethod
    async def create(self, create_dto: CreateContestTaskDto) -> ContestTask: ...
    @abstractmethod
    async def read(self, uuid: UUID) -> ContestTask: ...
    @abstractmethod
    async def read_all(self, uuids: list[UUID]) -> list[ContestTask]: ...
    @abstractmethod
    async def update(self, task: ContestTask) -> ContestTask: ...
    @abstractmethod
    async def delete(self, task: ContestTask) -> ContestTask: ...
