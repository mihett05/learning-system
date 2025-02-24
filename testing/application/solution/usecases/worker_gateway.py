from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from uuid import UUID


@dataclass
class WorkerMessage:
    solution_uuid: UUID
    task_uuid: UUID


class WorkerGateway(metaclass=ABCMeta):
    @abstractmethod
    async def run_solution(self, message: WorkerMessage): ...
