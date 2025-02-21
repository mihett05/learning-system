from dataclasses import dataclass
from uuid import UUID

@dataclass
class ReadSolutionDto:
    task_uuid: UUID
    page: int
    page_size: int

@dataclass
class CreateSolutionDto:
    uuid: UUID
    file: str
