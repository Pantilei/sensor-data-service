import uvicorn
import uvloop

from sds.core.configs import configs

uvloop.install()

uvicorn.run(
    "sds.app:app",
    host="0.0.0.0",
    port=8000,
    lifespan="on",
    reload=configs.DEBUG,
    workers=1,
)  # noqa: S104
