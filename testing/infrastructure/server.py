from infrastructure.http.app import create_app
from infrastructure.providers.container import create_container
from infrastructure.config import get_config

config = get_config()
container = create_container()
app = create_app(container, config)
