from typing import AsyncIterator

from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from loguru import logger

from sds.core.configs import configs
from sds.db.database import DB


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator:
    logger.info("Connecting to mongo database")
    await DB.connect(url=configs.SERVICE_MONGO)
    yield
    logger.info("Disconnecting from mongo database")
    await DB.disconnect()
