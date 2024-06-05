import base64
import binascii
from datetime import datetime
import json
from typing import Any
from pydantic import BaseModel, field_validator

from sds.schemas.sensors import SensorData


class _Message(BaseModel):
    attributes: dict[str, Any]
    data: SensorData
    message_id: str
    publish_time: str

    @field_validator("data", mode="before")
    @classmethod
    def decode_data(cls, sensor_b64_data: str) -> SensorData:
        try:
            decoded_data = base64.b64decode(sensor_b64_data, validate=True).decode()
        except binascii.Error:
            raise ValueError("Invalid base64 data")
        try:
            decoded_json = json.loads(decoded_data)
        except json.JSONDecodeError as jde:
            raise ValueError(str(jde))

        timestamp = datetime.fromisoformat(decoded_json["Time"])
        return SensorData(
            timestamp=timestamp,
            sensor_id=decoded_json["v0"],
            dwell_time=decoded_json["v18"],
        )


class GooglePubSubMessage(BaseModel):
    message: _Message
    subscription: str
