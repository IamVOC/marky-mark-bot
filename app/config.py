from pydantic_settings import BaseSettings, SettingsConfigDict

from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    TOKEN: str
    WEB_SERVER_HOST: str
    WEB_SERVER_PORT: int
    WEBHOOK_PATH: str


@lru_cache
def get_settings() -> Settings:
    return Settings()
