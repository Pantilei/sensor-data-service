from fastapi.routing import APIRouter
from sds.api.routes import sensors_data


router = APIRouter(prefix="/api")

router.include_router(sensors_data.router, prefix="/sensors-data", tags=["sensor"])
