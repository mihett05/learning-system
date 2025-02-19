from dishka import Provider, provide_all, Scope

from application.contest_tasks.usecases import ContestTaskReadUseCase


class UseCasesProvider(Provider):
    scope = Scope.REQUEST

    # для каждого модулю делаете по отдельному provide_all

    contest_tasks = provide_all(ContestTaskReadUseCase)
