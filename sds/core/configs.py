from pydantic import MongoDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    DEBUG: bool = True
    ALLOWED_HOSTS: str = ""
    ALLOWED_ORIGIN_REGEX: str = r".*"
    # Application
    APP_NAME: str = "sds"
    APP_VERSION: str
    APP_DESCRIPTION: str = "Sensor Data Service"
    # Services
    SERVICE_MONGO: MongoDsn

    def __repr__(self) -> str:
        return self.model_dump_json(indent=2)[2:][:-2]


configs = Settings()  # type: ignore
