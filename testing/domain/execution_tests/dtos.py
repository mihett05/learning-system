from dataclasses import dataclass
from uuid import UUID

from .enums import ExecutionTestTypeEnum


@dataclass
class CreateExecutionTestDto:
    title: str
    file: str
    type: ExecutionTestTypeEnum

@dataclass
class ReadExecutionTestDto:
    task_uuid: UUID
    page: int
    page_size: int
