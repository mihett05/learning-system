from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from uuid import UUID

from testing.domain.solution.dtos import CreateSolutionDto
from testing.domain.solution.entities import Solution
from testing.domain.solution.repositories import SolutionRepository

@dataclass
class WorkerMessage:
    solution_uuid: UUID
    task_uuid: UUID

class WorkerGateway(metaclass=ABCMeta):
    @abstractmethod
    def run_solution(self, message: WorkerMessage): ...


class CreateSolutionUsecase:
    def __init__(self, repository: SolutionRepository, gateway: WorkerGateway):
        self.__repository =  repository
        self.__gateway = gateway

    async def __call__(self, dto: CreateSolutionDto) -> Solution:
        solution = await self.__repository.create(dto)
        await self.__submit(solution.uuid, dto.task_uuid)
        return solution

    async def __submit(self, solution_uuid: UUID, task_uuid: UUID):
        self.__gateway.run_solution(WorkerMessage(solution_uuid, task_uuid))
