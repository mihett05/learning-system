from dataclasses import dataclass
from uuid import UUID

from .enums import ExecutionTestTypeEnum


@dataclass
class CreateExecutionTestDto:
    time_limit: int
    memory_limit: int
    file: str
    type: ExecutionTestTypeEnum

@dataclass
class ReadExecutionTestDto:
    task_guid: UUID
    page: int
    page_size: int
