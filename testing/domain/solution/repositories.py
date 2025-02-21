from abc import ABCMeta, abstractmethod
from uuid import UUID

from .dtos import CreateSolutionDto
from .dtos import ReadSolutionDto
from .entities import Solution


class SolutionRepository(metaclass=ABCMeta):
    @abstractmethod
    async def create(self, dto: CreateSolutionDto) -> Solution: ...
    @abstractmethod
    async def read(self, uuid: UUID) -> Solution: ...
    @abstractmethod
    async def update(self, solution: Solution) -> Solution: ...
    @abstractmethod
    async def read_all(self, dto: ReadSolutionDto) -> list[Solution]: ...
