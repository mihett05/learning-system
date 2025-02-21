from dataclasses import dataclass
from uuid import UUID

@dataclass
class ReadSolutionDTO:
    task_uuid: UUID
    page: int
    page_size: int

@dataclass
class CreateSolutionDTO:
    uuid: UUID
    file: str
