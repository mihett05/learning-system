from dataclasses import dataclass
from uuid import UUID

from domain.solution.entities import Result


@dataclass
class UpdateSolutionDto:
    result: Result
    solution_uuid: UUID
