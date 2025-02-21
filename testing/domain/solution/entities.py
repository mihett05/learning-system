from enum import Enum
from dataclasses import dataclass, field
from uuid import UUID
from datetime import datetime
from ..execution_tests.entities import ExecutionTest

class ResultTypeEnum(Enum):
    SHOW_ALL = "SHOW_ALL"
    SHOW_LAST_EXECUTION_RESULT = "SHOW_LAST_EXECUTION_RESULT"
    SHOW_HAS_PASSED_ONLY = "SHOW_HAS_PASSED_ONLY"


class ExecutionTestResultEnum(Enum):
    PASSED = "PASSED"
    RUNTIME_ERROR = "RUNTIME_ERROR"
    WRONG_ANSWER = "WRONG_ANSWER"
    PRESENTATION_ERROR = "PRESENTATION_ERROR"
    TIME_LIMIT_EXCEEDED = "TIME_LIMIT_EXCEEDED"
    MEMORY_LIMIT_EXCEEDED = "MEMORY_LIMIT_EXCEEDED"
    SECURITY_VIOLATION = "SECURITY_VIOLATION"
    COMPILATION_ERROR = "COMPILATION_ERROR"


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
    result: Result
    created_at: datetime = field(default_factory=datetime.utcnow)
