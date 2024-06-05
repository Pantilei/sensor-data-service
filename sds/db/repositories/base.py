from motor.core import AgnosticCollection, AgnosticClient


class BaseRepository:
    client: AgnosticClient
    collection: AgnosticCollection

    def __init__(self, db_name: str, coll_name: str) -> None:
        self._db_name = db_name
        self._coll_name = coll_name

    async def __connect__(self, __db_client: AgnosticClient) -> None:
        self.client = __db_client
        self.collection = __db_client[self._db_name][self._coll_name]
