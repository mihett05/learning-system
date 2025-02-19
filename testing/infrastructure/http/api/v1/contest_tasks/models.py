from datetime import datetime
from uuid import UUID

from domain.execution_tests.entities import ExecutionTest
from infrastructure.http.api.models import CamelModel


class ContestTaskModel(CamelModel):
    task_info_id: UUID
    time_limit: int
    memory_limit: int
    execution_tests: list[ExecutionTest]

    created_at: datetime
