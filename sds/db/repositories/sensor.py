from sds.db.repositories.base import BaseRepository
from sds.schemas.sensors import SensorData, SensorDataDB


class SensorsDataRepository(BaseRepository):
    async def create_sensor_data(self, sensor_data: SensorData) -> str:
        result = await self.collection.insert_one(sensor_data.model_dump())
        return str(result.inserted_id)

    async def get_sensor_data(
        self, skip: int = 0, limit: int = 100
    ) -> list[SensorDataDB]:
        sort = [("timestamp", -1)]
        sensor_data = []
        async for row in self.collection.find({}, sort=sort, skip=skip, limit=limit):
            sensor_data.append(
                SensorDataDB(
                    oid=str(row["_id"]),
                    timestamp=row["timestamp"],
                    sensor_id=row["sensor_id"],
                    dwell_time=row["dwell_time"],
                )
            )
        return sensor_data
