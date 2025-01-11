from abc import ABC
from typing import (
    Any,
    Dict,
    Generic,
    MutableMapping,
    Optional,
    Sequence,
    Tuple,
    Union,
)

from django.db.models import QuerySet
from asgiref.sync import sync_to_async

from .async_repository import (
    AsyncAbstractEditRepository,
    AsyncAbstractFetchRepository,
    AsyncAbstractRepository, TModel,
)

class AsyncAbstractFetchService(Generic[TModel]):
    def __init__(self, repository: Union[AsyncAbstractFetchRepository]):
        self._repository = repository

    @property
    def model(self) -> TModel:
        return self._repository.model

    async def aget(self, *args, **kwargs) -> TModel:
        return await self._repository.aget(*args, **kwargs)

    async def afilter(self, *args, **kwargs) -> QuerySet[TModel]:
        return await self._repository.filter(*args, **kwargs)

    async def aall(self) -> QuerySet[TModel]:
        return await self._repository.aall()

    async def acount(self, *args, **kwargs) -> int:
        return await self._repository.acount(*args, **kwargs)

    async def aexists(self, *args, **kwargs) -> bool:
        return await self._repository.aexists(*args, **kwargs)


class AsyncAbstractEditService(Generic[TModel]):
    def __init__(self, repository: AsyncAbstractEditRepository[TModel]):
        self._repository = repository

    @property
    def model(self) -> TModel:
        return self._repository.model

    async def acreate(self, **kwargs) -> TModel:
        return await self._repository.acreate(**kwargs)

    async def aget_or_create(self, defaults: MutableMapping[str, Any], **kwargs) -> Tuple[TModel, bool]:
        return await self._repository.aget_or_create(defaults=defaults, **kwargs)

    async def aupdate(self, instance: TModel, **kwargs) -> TModel:
        return await self._repository.aupdate(instance, **kwargs)

    async def adelete(self, instance: TModel) -> None:
        return await self._repository.adelete(instance)

    async def abulk_create(self, instances: Sequence[TModel]) -> Sequence[TModel]:
        return await self._repository.abulk_create(instances)

    async def abulk_update(self, instances: Sequence[TModel], fields: Sequence[str], batch_size: Optional[int] = None) -> int:
        return await self._repository.abulk_update(instances=instances, fields=fields, batch_size=batch_size)


class AsyncAbstractService(ABC, Generic[TModel], AsyncAbstractFetchService[TModel], AsyncAbstractEditService[TModel]):
    @property
    def model(self) -> TModel:
        return self._repository.model

    def __init__(self, repository):
        self._repository = repository