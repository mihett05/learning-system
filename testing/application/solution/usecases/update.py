from testing.application.solution import UpdateSolutionDto
from testing.domain.solution.repositories import SolutionRepository


class UpdateSolutionUsecase:
    def __init__(self, repository: SolutionRepository):
        self.__repository = repository

    async def __call__(self, dto: UpdateSolutionDto):
        solution = await self.__repository.read(dto.solution_uuid)
        solution.result = dto.result
        return await self.__repository.update(solution)
