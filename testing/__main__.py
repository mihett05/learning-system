import argparse
from enum import Enum
from uvicorn import run
from infrastructure.config import get_config


class ServiceMode(str, Enum):
    SERVER = "server"
    WORKER = "worker"


parser = argparse.ArgumentParser(prog="Testing service")
parser.add_argument("mode", default=ServiceMode.SERVER, type=ServiceMode)
args = parser.parse_args()
mode = args.mode

if __name__ == "__main__":
    config = get_config()
    if mode == ServiceMode.SERVER:
        run(
            "infrastructure.server:app",
            port=config.server_port,
            host=config.server_host,
            reload=True,
        )
    else:
        print("worker is not implemented yet")
