from fastapi import APIRouter, Query

from sds.db.db import DB
from sds.schemas.google_pubsub import GooglePubSubMessage
from sds.schemas.sensors import SensorDataDB


router = APIRouter()


@router.get("")
async def get_sensor_data(
    skip: int = Query(0), limit: int = Query(100, le=100)
) -> list[SensorDataDB]:
    """Get sensors data"""
    return await DB.sensor_data_repo.get_sensor_data(skip=skip, limit=limit)


@router.post("")
async def handle_google_pubsub(pubsub_message: GooglePubSubMessage) -> str:
    """Handle google pubsub message"""
    return await DB.sensor_data_repo.create_sensor_data(pubsub_message.message.data)
