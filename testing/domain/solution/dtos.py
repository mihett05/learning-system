from dataclasses import dataclass
from uuid import UUID

@dataclass
class SolutionReadDTO:
    task_guid: UUID
    page: int
    page_size: int

@dataclass
class SolutionCreateDTO:
    id: UUID
    file: str