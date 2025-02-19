from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import func, ForeignKey, String, Enum, DateTime

from domain.execution_tests.enums import ExecutionTestTypeEnum
from infrastructure.database.postgres import Base


class ExecutionTestDbModel(Base):
    __tablename__ = "executions_tests"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    task_info_id: Mapped[UUID] = mapped_column(
        ForeignKey("contest_tasks.task_info_id", ondelete="CASCADE")
    )

    title: Mapped[str]
    type: Mapped[ExecutionTestTypeEnum] = mapped_column(Enum(ExecutionTestTypeEnum))

    archive: Mapped[str | None] = mapped_column(default=None)
    input_files: Mapped[list[str]] = mapped_column(ARRAY(String), server_default="{}")
    output_files: Mapped[list[str]] = mapped_column(ARRAY(String), server_default="{}")
    test_file: Mapped[str | None] = mapped_column(default=None)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
