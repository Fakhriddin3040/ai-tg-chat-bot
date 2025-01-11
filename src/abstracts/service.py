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

from .repository import (
    AbstractEditRepository,
    AbstractFetchRepository,
    AbstractRepository, TModel,
)

class AbstractFetchService(Generic[TModel]):
    def __init__(self, repository: Union[AbstractFetchRepository]):
        self._repository = repository

    @property
    def model(self) -> TModel:
        return self._repository.model

    def get(self, *args, **kwargs) -> TModel:
        return self._repository.get(*args, **kwargs)

    def filter(self, *args, **kwargs) -> QuerySet[TModel]:
        return self._repository.filter(*args, **kwargs)

    def all(self) -> QuerySet[TModel]:
        return self._repository.all()

    def count(self, *args, **kwargs) -> int:
        return self._repository.count(*args, **kwargs)

    def exists(self, *args, **kwargs) -> bool:
        return self._repository.exists(*args, **kwargs)


class AbstractEditService(Generic[TModel]):
    def __init__(self, repository: AbstractEditRepository[TModel]):
        self._repository = repository

    @property
    def model(self) -> TModel:
        return self._repository.model

    def create(self, **kwargs) -> TModel:
        return self._repository.create(**kwargs)

    def get_or_create(self, defaults: MutableMapping[str, Any], **kwargs) -> Tuple[TModel, bool]:
        return self._repository.get_or_create(defaults=defaults, **kwargs)

    def update(self, **kwargs) -> TModel:
        return self._repository.update(**kwargs)

    def delete(self, **kwargs) -> None:
        return self._repository.delete(**kwargs)

    def bulk_create(self, instances: Sequence[TModel]) -> Sequence[TModel]:
        return self._repository.bulk_create(instances)

    def bulk_update(self, instances: Sequence[TModel], fields: Sequence[str], batch_size: Optional[int] = None) -> int:
        return self._repository.bulk_update(instances=instances, fields=fields, batch_size=batch_size)


class AbstractService(ABC, Generic[TModel], AbstractFetchService[TModel], AbstractEditService[TModel]):
    @property
    def model(self) -> TModel:
        return self._repository.model

    def __init__(self, repository):
        self._repository = repository

