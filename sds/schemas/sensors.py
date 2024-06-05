from datetime import datetime
from pydantic import BaseModel


class SensorData(BaseModel):
    timestamp: datetime
    sensor_id: int
    dwell_time: float


class SensorDataDB(SensorData):
    oid: str
