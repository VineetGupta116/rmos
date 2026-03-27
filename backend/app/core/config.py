from functools import lru_cache

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    app_name: str = 'ResearchMaster OS API'
    app_env: str = 'development'
    app_version: str = '1.0.0'

    backend_host: str = '0.0.0.0'
    backend_port: int = 8000
    backend_cors_origins: list[str] = Field(default_factory=lambda: ['http://localhost:3000'])

    @field_validator('backend_cors_origins', mode='before')
    @classmethod
    def parse_cors(cls, value: str | list[str]) -> list[str]:
        if isinstance(value, str):
            return [origin.strip() for origin in value.split(',') if origin.strip()]
        return value


@lru_cache
def get_settings() -> Settings:
    return Settings()
