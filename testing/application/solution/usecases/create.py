from uuid import UUID

from application.solution.usecases.worker_gateway import WorkerGateway
from domain.solution.dtos import CreateSolutionDto
from domain.solution.entities import Solution
from domain.solution.repositories import SolutionRepository


class CreateSolutionUsecase:
    def __init__(self, repository: SolutionRepository, gateway: WorkerGateway):
        self.__repository = repository
        self.__gateway = gateway

    async def __call__(self, dto: CreateSolutionDto) -> Solution:
        solution = await self.__repository.create(dto)
        await self.__submit(solution.uuid, dto.task_uuid)
        return solution

    async def __submit(self, solution_uuid: UUID, task_uuid: UUID):
        self.__gateway.run_solution(WorkerMessage(solution_uuid, task_uuid))
