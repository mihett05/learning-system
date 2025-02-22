from dishka import make_async_container, AsyncContainer, Provider

from .repositories import RepositoriesProvider
from infrastructure.providers.config import ConfigProvider
from infrastructure.providers.container import get_container_application


def get_container_mocks() -> list[Provider]:
    return [
        ConfigProvider(),
        RepositoriesProvider(),
    ]


def create_test_container() -> AsyncContainer:
    return make_async_container(
        *get_container_mocks(),
        *get_container_application(),
    )
