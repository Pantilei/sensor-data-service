from pydantic_core import MultiHostUrl


class DB:
    @classmethod
    async def connect(cls, url: MultiHostUrl) -> None:
        """Disconnect from db"""

    @classmethod
    async def disconnect(cls) -> None:
        """Disconnect from DB"""
