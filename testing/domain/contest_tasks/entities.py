from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

from domain.execution_tests.entities import ExecutionTest


@dataclass
class ContestTask:
    task_info_id: UUID
    time_limit: int
    memory_limit: int
    execution_tests: list[ExecutionTest]

    created_at: datetime = field(default_factory=datetime.utcnow)
