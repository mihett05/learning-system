from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func, DateTime

from infrastructure.database.postgres import Base
from ..executions_tasks.models import ExecutionTestDbModel


class ContestTaskDbModel(Base):
    __tablename__ = "contest_tasks"

    task_info_id: Mapped[UUID] = mapped_column(primary_key=True)
    time_limit: Mapped[int]
    memory_limit: Mapped[int]

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    execution_tests: Mapped[list[ExecutionTestDbModel]] = relationship()
