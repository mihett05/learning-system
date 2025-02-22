from dishka import make_async_container, AsyncContainer, Provider

from .usecases import UseCasesProvider
from .config import ConfigProvider
from .database import DatabaseProvider
from .repositories import RepositoriesProvider


def get_container_infrastructure() -> list[Provider]:
    return [
        ConfigProvider(),
        DatabaseProvider(),
        RepositoriesProvider(),
    ]


def get_container_application() -> list[Provider]:
    return [
        UseCasesProvider(),
    ]


def create_container() -> AsyncContainer:
    return make_async_container(
        *get_container_infrastructure(),
        *get_container_application(),
    )
