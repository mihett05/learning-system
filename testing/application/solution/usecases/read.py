from uuid import UUID

from testing.domain.solution.entities import Solution
from testing.domain.solution.repositories import SolutionRepository


class ReadSolutionUsecase:
    def __init__(self, repository: SolutionRepository):
        self.__repository = repository

    async def __call__(self, uuid: UUID) -> Solution:
        return await self.__repository.read(uuid)
