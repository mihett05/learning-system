from dataclasses import dataclass, field
from uuid import UUID
from datetime import datetime

from ..execution_tests.entities import ExecutionTest
from .enums import ExecutionTestResultEnum, ResultTypeEnum


@dataclass
class ResultTry:
    uuid: UUID
    state: ExecutionTestResultEnum
    description: str
    description_short: str
    execution_tests: ExecutionTest
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Result:
    uuid: UUID
    score: int
    title: str
    type: ResultTypeEnum
    result_try: ResultTry
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Solution:
    uuid: UUID
    file: str
    result: Result | None
    created_at: datetime = field(default_factory=datetime.utcnow)
