from dishka import Provider, provide, Scope

from domain.contest_tasks.repositories import ContestTaskRepository
from infrastructure.mocks.repositories.contest_task import ContestTaskMemoryRepository


class RepositoriesProvider(Provider):
    scope = Scope.APP  # APP, так как storage у них у всех общий будет

    contest_task = provide(
        source=ContestTaskMemoryRepository, provides=ContestTaskRepository
    )
