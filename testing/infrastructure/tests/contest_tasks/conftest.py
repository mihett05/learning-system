from uuid import uuid4

import pytest_asyncio
from dishka import AsyncContainer

from domain.contest_tasks.dtos import CreateContestTaskDto
from domain.contest_tasks.entities import ContestTask
from domain.contest_tasks.repositories import ContestTaskRepository
from application.contest_tasks.usecases import ReadContestTaskUseCase


@pytest_asyncio.fixture
async def contest_tasks_repository(container: AsyncContainer) -> ContestTaskRepository:
    async with container() as nested:
        yield await nested.get(ContestTaskRepository)


@pytest_asyncio.fixture
async def read_contest_task_usecase(
    container: AsyncContainer,
) -> ReadContestTaskUseCase:
    async with container() as nested:
        yield await nested.get(ReadContestTaskUseCase)


@pytest_asyncio.fixture
async def created_contest_task(
    contest_tasks_repository: ContestTaskRepository,
) -> ContestTask:
    return await contest_tasks_repository.create(
        CreateContestTaskDto(
            task_info_id=uuid4(),
            time_limit=10,
            memory_limit=10,
        )
    )
