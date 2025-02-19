from fastapi import APIRouter

from .contest_tasks import contest_tasks_router

v1_router = APIRouter()
v1_router.include_router(contest_tasks_router, prefix="/contest-tasks")
