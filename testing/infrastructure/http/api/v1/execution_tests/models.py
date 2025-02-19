from datetime import datetime
from uuid import UUID

from domain.execution_tests.enums import ExecutionTestTypeEnum
from infrastructure.http.api.models import CamelModel


class ExecutionTestModel(CamelModel):
    id: UUID
    title: str
    type: ExecutionTestTypeEnum

    created_at: datetime
