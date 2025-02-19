from abc import ABCMeta
from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

from .enums import ExecutionTestTypeEnum


@dataclass
class ExecutionTest(metaclass=ABCMeta):
    id: UUID
    title: str
    type: ExecutionTestTypeEnum

    created_at: datetime = field(default_factory=datetime.utcnow)
