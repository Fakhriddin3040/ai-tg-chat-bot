from abc import ABC
from typing import (
    Any,
    Generic,
    Iterable,
    MutableMapping,
    Optional,
    Sequence,
    Tuple,
    Union,
    TypeVar
)

from django.db import models


TModel = TypeVar("TModel", bound=models.Model)


class AbstractFetchRepository(Generic[TModel]):
    model: TModel

    def get(self, *args, **kwargs) -> Union[TModel, None]:
        res = self.filter(*args, **kwargs)
        if res.count() > 1:
            raise self.model.MultipleObjectsReturned
        return res.first()

    def filter(self, *args, **kwargs) -> models.QuerySet[TModel]:
        return self.all().filter(*args, **kwargs)

    def all(self) -> models.QuerySet[TModel]:
        return self.model.objects.all()

    def count(self, *args, **kwargs) -> int:
        return self.filter(*args, **kwargs).count()

    def exists(self, *args, **kwargs) -> bool:
        return self.filter(**kwargs).exists()


class AbstractEditRepository(Generic[TModel]):
    model: TModel

    def create(self, **kwargs) -> TModel:
        return self.model.objects.create(**kwargs)

    def get_or_create(self, defaults: Optional[MutableMapping[str, Any]] = None, **kwargs) -> Tuple[TModel, bool]:
        return self.model.objects.get_or_create(defaults=defaults, **kwargs)

    def update(self, instance: TModel, **kwargs) -> TModel:
        for key, value in kwargs.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def delete(self, instance: TModel):
        instance.delete()

    def bulk_create(self, instances) -> list[TModel]:
        return self.model.objects.bulk_create(instances)

    def bulk_update(self, instances: Iterable[TModel], fields: Sequence[str], batch_size: Optional[int]) -> int:
        return self.model.objects.bulk_update(objs=instances, fields=fields, batch_size=batch_size)

    def create_or_update(self, **kwargs) -> Tuple[TModel, bool]:
        instance, created = self.model.objects.update_or_create(**kwargs)
        return instance, created



class AbstractRepository(Generic[TModel], AbstractFetchRepository[TModel], AbstractEditRepository[TModel], ABC):
    def update_with_query(self, data: dict, **filters) -> int:
        return self.filter(**filters).update(data)

    def delete_with_query(self, **filters) -> tuple[int, dict[str, int]]:
        return self.filter(**filters).delete()
