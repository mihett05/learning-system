from infrastructure.http.api.retort import pydantic_retort

from domain.execution_tests.entities import ExecutionTest
from .models import ExecutionTestModel

retort = pydantic_retort.extend(recipe=[])

map_to_pydantic = retort.get_converter(ExecutionTest, ExecutionTestModel)
