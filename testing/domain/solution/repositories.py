from abc import ABCMeta, abstractmethod
from uuid import UUID

from .dtos import SolutionCreateDTO
from .dtos import SolutionReadDTO
from .entities import Solution


class SolutionRepository(metaclass=ABCMeta):
    @abstractmethod
    async def create(self, dto: SolutionCreateDTO) -> Solution: ...
    @abstractmethod
    async def read(self, guid: UUID) -> Solution: ...
    @abstractmethod
    async def update(self, solution: Solution) -> Solution: ...
    @abstractmethod
    async def read_all(self, dto: SolutionReadDTO) -> list[Solution]: ...
