from adaptix import P
from adaptix.conversion import link_function, coercer, allow_unlinked_optional

from infrastructure.database.mappers import postgres_retort
from .models import ContestTaskDbModel
from domain.contest_tasks.entities import ContestTask
from domain.contest_tasks.dtos import CreateContestTaskDto

from domain.execution_tests.entities import ExecutionTest

from ..executions_tasks import mappers as execution_tasks_mappers
from ..executions_tasks.models import ExecutionTestDbModel

retort = postgres_retort.extend(recipe=[])

map_from_db = retort.get_converter(
    ContestTaskDbModel,
    ContestTask,
    recipe=[
        coercer(ExecutionTestDbModel, ExecutionTest, execution_tasks_mappers.map_to_db)
    ],
)
map_to_db = retort.get_converter(
    ContestTask,
    ContestTaskDbModel,
    recipe=[
        link_function(lambda contest_task: [], P[ContestTaskDbModel].execution_tests)
    ],
)


@retort.impl_converter(
    recipe=[
        link_function(lambda dto: [], P[ContestTask].execution_tests),
        allow_unlinked_optional(P[ContestTask].created_at),
    ]
)
def map_create_db(dto: CreateContestTaskDto) -> ContestTask: ...
