from adaptix.conversion import coercer

from infrastructure.http.api.retort import pydantic_retort

from domain.contest_tasks.entities import ContestTask, ExecutionTest
from .models import ContestTaskModel
from ..execution_tests.models import ExecutionTestModel
from ..execution_tests import mappers as execution_tests_mappers


map_to_pydantic = pydantic_retort.get_converter(
    ContestTask,
    ContestTaskModel,
    recipe=[
        coercer(
            ExecutionTest, ExecutionTestModel, execution_tests_mappers.map_to_pydantic
        )
    ],
)
