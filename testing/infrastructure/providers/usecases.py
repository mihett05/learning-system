from dishka import Provider, provide_all, Scope

from application.contest_tasks.usecases import (
    CreateContestTaskUseCase,
    ReadContestTaskUseCase,
    ReadAllContestTaskUseCase,
    UpdateContestTaskUseCase,
    DeleteContestTaskUseCase,
)


class UseCasesProvider(Provider):
    scope = Scope.REQUEST

    # для каждого модулю делаете по отдельному provide_all

    contest_tasks = provide_all(
        CreateContestTaskUseCase,
        ReadContestTaskUseCase,
        ReadAllContestTaskUseCase,
        UpdateContestTaskUseCase,
        DeleteContestTaskUseCase,
    )
