import json

from config import get_config


def save(user_registry: dict):
    with open(get_config().DB, "w") as file:
        return json.dump(user_registry, file, indent=4, ensure_ascii=False)


def load() -> dict:
    with open(get_config().DB, "r") as file:
        return json.load(file)
