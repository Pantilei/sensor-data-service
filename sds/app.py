from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sds.api.api import router
from sds.core.configs import configs
from sds.core.events import lifespan

app = FastAPI(
    debug=configs.DEBUG,
    title=configs.APP_NAME,
    description=configs.APP_DESCRIPTION,
    version=configs.APP_VERSION,
    lifespan=lifespan,
)

app.get("/healthy", include_in_schema=False)(lambda: True)
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=configs.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origin_regex=configs.ALLOWED_ORIGIN_REGEX,
)
