from fastapi.routing import APIRouter
from sds.api.routes import dwell_time


router = APIRouter(prefix="/api")

router.include_router(dwell_time.router, prefix="/dwell-time")
