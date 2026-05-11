from urllib.parse import urlparse, urlunparse, parse_qsl, urlencode

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str

    model_config = SettingsConfigDict(env_file=".env")

    @field_validator("DATABASE_URL")
    @classmethod
    def normalize_for_asyncpg(cls, v: str) -> str:
        parsed = urlparse(v)

        scheme = parsed.scheme
        if scheme == "postgresql":
            scheme = "postgresql+asyncpg"

        libpq_only = {"channel_binding"}
        rename = {"sslmode": "ssl"}
        new_query = urlencode([
            (rename.get(k, k), val)
            for k, val in parse_qsl(parsed.query)
            if k not in libpq_only
        ])

        return urlunparse(parsed._replace(scheme=scheme, query=new_query))


settings = Settings()
