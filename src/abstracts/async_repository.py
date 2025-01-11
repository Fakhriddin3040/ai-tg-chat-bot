from typing import Optional, Tuple, Sequence, Generic
from django.db import models
from asgiref.sync import sync_to_async
from src.abstracts.repository import TModel


class AsyncAbstractFetchRepository(Generic[TModel]):
    model: TModel

    async def aget(self, *args, **kwargs) -> Optional[TModel]:
        res = await self.filter(*args, **kwargs)
        if res.count() > 1:
            raise self.model.MultipleObjectsReturned
        return await res.aget()

    def filter(self, *args, **kwargs) -> models.QuerySet:
        return self.model.objects.filter(*args, **kwargs)

    async def aall(self) -> models.QuerySet:
        return await sync_to_async(self.model.objects.all)()

    async def acount(self, *args, **kwargs) -> int:
        return await sync_to_async(self.filter)(*args, **kwargs).acount()

    async def aexists(self, *args, **kwargs) -> bool:
        return await self.filter(**kwargs).aexists()

class AsyncAbstractEditRepository(Generic[TModel]):
    model: TModel

    async def acreate(self, **kwargs) -> TModel:
        return await self.model.objects.acreate(**kwargs)

    async def aget_or_create(self, defaults: Optional[dict] = None, **kwargs) -> Tuple[TModel, bool]:
        return await self.model.objects.aget_or_create(defaults=defaults, **kwargs)

    @staticmethod
    async def aupdate(instance: TModel, **kwargs) -> TModel:
        for key, value in kwargs.items():
            setattr(instance, key, value)
        await instance.asave()
        return instance

    @staticmethod
    async def adelete(instance: TModel):
        await instance.adelete()

    async def abulk_create(self, instances: Sequence[TModel]) -> Sequence[TModel]:
        return await self.model.objectsabulk_create(instances)

    async def abulk_update(self, instances: Sequence[TModel], fields: Sequence[str], batch_size: Optional[int]) -> int:
        return await self.model.objectsabulk_update(objs=instances, fields=fields, batch_size=batch_size)

    async def acreate_or_update(self, **kwargs) -> Tuple[TModel, bool]:
        instance, created = await self.model.objects.aupdate_or_create(**kwargs)
        return instance, created


class AsyncAbstractRepository(AsyncAbstractFetchRepository[TModel], AsyncAbstractEditRepository[TModel]):
    models: TModel
