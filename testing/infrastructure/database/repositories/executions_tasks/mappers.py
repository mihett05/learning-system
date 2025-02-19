from infrastructure.database.mappers import postgres_retort

from domain.execution_tests.entities import ExecutionTest
from .models import ExecutionTestDbModel

retort = postgres_retort.extend(recipe=[])

map_to_db = retort.get_converter(ExecutionTestDbModel, ExecutionTest)
