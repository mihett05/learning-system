from abc import ABCMeta, abstractmethod


class Transaction(metaclass=ABCMeta):
    # если чё, после коммита или ролбека транзакции нельзя больше с ней ничего делать, она закрытой становится
    # учитывайте это, когда будете писать юзкейсы
    @abstractmethod
    async def commit(self): ...
    @abstractmethod
    async def rollback(self): ...


class TransactionsGateway(metaclass=ABCMeta):
    @abstractmethod
    async def __aenter__(self) -> Transaction: ...
    @abstractmethod
    def nested(self) -> "TransactionsGateway": ...
    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb): ...
