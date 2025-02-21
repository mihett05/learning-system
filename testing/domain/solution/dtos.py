from dataclasses import dataclass
from uuid import UUID

@dataclass
class SolutionReadDTO:
    task_uuid: UUID
    page: int
    page_size: int

@dataclass
class SolutionCreateDTO:
    uuid: UUID
    file: str
