from domain.solution.entities import Solution
from domain.solution.repositories import SolutionRepository
from domain.solution.dtos import ReadSolutionDto


class ReadAllSolutionUsecase:
    def __init__(self, repository: SolutionRepository):
        self.__repository = repository

    async def __call__(self, dto: ReadSolutionDto) -> list[Solution]:
        return await self.__repository.read_all(dto)
