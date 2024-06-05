import asyncio
import inspect
from typing import ClassVar, Iterator

from motor.core import AgnosticClient
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_core import MultiHostUrl

from sds.db.db import DB
from sds.db.repositories.base import BaseRepository


class DBClient:
    client: ClassVar[AgnosticClient]

    @classmethod
    async def connect(cls, url: MultiHostUrl) -> None:
        cls.client = AsyncIOMotorClient(str(url))
        async with asyncio.TaskGroup() as tg:
            for _, repo in cls._get_repositories():
                tg.create_task(repo.__connect__(cls.client))

    @classmethod
    def disconnect(cls) -> None:
        cls.client.close()

    @classmethod
    def _get_repositories(cls) -> Iterator[tuple[str, BaseRepository]]:
        def _is_repository(obj) -> bool:
            return issubclass(obj.__class__, BaseRepository)

        print(inspect.getmembers(DB, _is_repository))
        for name, attr in inspect.getmembers(DB, _is_repository):
            yield name, attr
