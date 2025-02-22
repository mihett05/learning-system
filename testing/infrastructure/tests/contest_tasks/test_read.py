import pytest

from uuid import uuid4

from domain.contest_tasks.entities import ContestTask
from domain.contest_tasks.exceptions import ContestTasksNotFoundException
from application.contest_tasks.usecases import ReadContestTaskUseCase


@pytest.mark.asyncio
async def test_read_success(
    read_contest_task_usecase: ReadContestTaskUseCase,
    created_contest_task: ContestTask,
):
    task = await read_contest_task_usecase(created_contest_task.task_info_id)
    assert task.task_info_id == created_contest_task.task_info_id
    assert task.time_limit == created_contest_task.time_limit
    assert task.memory_limit == created_contest_task.memory_limit


@pytest.mark.asyncio
async def test_read_not_found(read_contest_task_usecase: ReadContestTaskUseCase):
    with pytest.raises(ContestTasksNotFoundException):
        await read_contest_task_usecase(uuid4())
