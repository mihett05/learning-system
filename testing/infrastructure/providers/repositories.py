from dishka import Provider, provide, Scope

from infrastructure.database.repositories.contest_tasks import (
    ContestTaskDatabaseRepository,
    ContestTaskRepository,
)


class RepositoriesProvider(Provider):
    scope = Scope.REQUEST

    contest_task = provide(
        source=ContestTaskDatabaseRepository, provides=ContestTaskRepository
    )
