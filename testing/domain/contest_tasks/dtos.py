from dataclasses import dataclass
from uuid import UUID


@dataclass
class CreateContestTaskDto:
    task_info_id: UUID
    time_limit: int
    memory_limit: int


@dataclass
class UpdateContestTaskDto:
    task_info_id: UUID
    time_limit: int | None
    memory_limit: int | None
