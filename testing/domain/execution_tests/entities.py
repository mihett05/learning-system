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
    file: str
    created_at: datetime = field(default_factory=datetime.utcnow)

@dataclass
class TargetLanguageTest(ExecutionTest):
    input_file: str = ""
    output_file: str = ""

@dataclass
class InputOutputTest(ExecutionTest):
    input_file: str = ""
    output_file: list[str] = field(default_factory=list)

@dataclass
class MakefileTest(ExecutionTest):
    archive: str = ""
