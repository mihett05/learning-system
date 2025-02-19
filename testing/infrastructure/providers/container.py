from dishka import make_async_container, AsyncContainer

from .usecases import UseCasesProvider
from .config import ConfigProvider
from .database import DatabaseProvider
from .repositories import RepositoriesProvider


def create_container() -> AsyncContainer:
    return make_async_container(
        ConfigProvider(),
        DatabaseProvider(),
        RepositoriesProvider(),
        UseCasesProvider(),
    )
