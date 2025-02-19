from abc import ABCMeta
from dataclasses import dataclass
from typing import Any, Callable, Generic, TypeVar

from sqlalchemy import Delete, Insert, Select, Update, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.interfaces import LoaderOption
from sqlalchemy.sql.base import Executable

from domain.exceptions import EntityAlreadyExists, EntityNotFound
from ..transactions import transaction_var

Id = TypeVar("Id")
Entity = TypeVar("Entity")
CreateEntity = TypeVar("CreateEntity")
ModelType = TypeVar("ModelType")


@dataclass
class PostgresRepositoryConfig(Generic[ModelType, Entity, Id]):
    model: type[ModelType]
    entity: type[Entity]
    entity_mapper: Callable[[ModelType], Entity]
    model_mapper: Callable[[Entity], ModelType]
    create_mapper: Callable[[Entity], ModelType] | None = None
    not_found_exception: type[EntityNotFound] = EntityNotFound
    already_exists_exception: type[EntityAlreadyExists] = EntityAlreadyExists

    def get_select_query(self, id: Id) -> Select:
        return self.add_where_id(select(self.model), id)

    def get_select_all_query(self) -> Select:
        return select(self.model).order_by(self.model.id)

    def add_where_entity(
        self, statement: Select | Update | Delete, entity: Entity
    ) -> Select | Update | Delete:
        return self.add_where_id(statement, self.extract_id_from_entity(entity))

    def add_where_id(
        self, statement: Select | Update | Delete, id: Id
    ) -> Select | Update | Delete:
        return statement.where(self.model.id == id)

    def extract_id_from_entity(self, entity: Entity) -> Id:
        return entity.id

    def extract_id_from_model(self, model: ModelType) -> Id:
        return model.id

    def add_options(self, statement: Executable) -> Executable:
        return statement.options(*self.get_options())

    def get_options(self) -> list[LoaderOption]:
        return []


class PostgresRepository(metaclass=ABCMeta):
    config: PostgresRepositoryConfig

    def __init__(self, session: AsyncSession, config: PostgresRepositoryConfig) -> None:
        self.session = session
        self.config = config

    async def get_models_from_query(self, query: Select) -> list[ModelType]:
        return list((await self.session.scalars(self.config.add_options(query))).all())

    async def get_entities_from_query(self, query: Select) -> list[Entity]:
        return [
            self.config.entity_mapper(model)
            for model in await self.get_models_from_query(query)
        ]

    async def run_query_and_get_scalar_or_none(
        self, query: Update | Insert | Delete
    ) -> ModelType | None:
        return (
            await self.session.execute(
                self.config.add_options(query.returning(self.config.model))
            )
        ).scalar_one_or_none()

    async def create_models(
        self, query: Insert, kwargs: list[dict[str, Any]]
    ) -> list[dict[str, Any]]:
        return list(
            (
                await self.session.scalars(
                    self.config.add_options(
                        query.values(kwargs).returning(self.config.model)
                    )
                )
            ).all()
        )

    async def read(self, id: Id) -> Entity:
        if model := await self.session.get(
            self.config.model,
            id,
            options=self.config.get_options(),
            populate_existing=True,
        ):
            return self.config.entity_mapper(model)
        raise self.config.not_found_exception()

    async def read_all(self) -> list[Entity]:
        return await self.get_entities_from_query(self.config.get_select_all_query())

    async def create(self, entity: CreateEntity | Entity) -> Entity:
        model = (self.config.create_mapper or self.config.model_mapper)(entity)
        try:
            self.session.add(model)
            if self._should_commit():
                await self.session.commit()
            await self.session.refresh(model)
            return await self.read(self.config.extract_id_from_model(model))
        except IntegrityError:
            raise self.config.already_exists_exception()

    async def update(self, entity: Entity) -> Entity:
        try:
            await self.read(self.config.extract_id_from_entity(entity))
        except EntityNotFound:
            raise self.config.not_found_exception()
        model = self.config.model_mapper(entity)
        await self.session.merge(model)
        if self._should_commit():
            await self.session.commit()
        return self.config.entity_mapper(model)

    async def delete(self, entity: Entity) -> Entity:
        if model := await self.session.get(
            self.config.model, self.config.extract_id_from_entity(entity)
        ):
            await self.session.delete(model)
            if self._should_commit():
                await self.session.commit()
            return entity
        raise self.config.not_found_exception()

    @staticmethod
    def _should_commit() -> bool:
        session = transaction_var.get()
        return session is None
