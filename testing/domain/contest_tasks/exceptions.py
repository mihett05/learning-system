from .entities import ContestTask
from ..exceptions import EntityNotFound, EntityAlreadyExists


class ContestTasksNotFoundException(EntityNotFound):
    def __init__(self):
        super().__init__(ContestTask)


class ContestTaskAlreadyExistsException(EntityAlreadyExists):
    def __init__(self):
        super().__init__(ContestTask)
