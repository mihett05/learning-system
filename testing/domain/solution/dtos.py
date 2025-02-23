from dataclasses import dataclass
from uuid import UUID

@dataclass
class ReadSolutionDto:
    task_uuid: UUID
    page: int
    page_size: int

@dataclass
class CreateSolutionDto:
    task_uuid: UUID
    file: str
