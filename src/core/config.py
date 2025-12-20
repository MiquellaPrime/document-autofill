from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class ServerConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class PostgresConfig(BaseModel):
    host: str
    port: int
    user: str
    password: str
    dbname: str

    @property
    def async_dsn(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"


class DatabaseConfig(BaseModel):
    postgres: PostgresConfig

    @property
    def url(self) -> str:
        return self.postgres.async_dsn

    echo: bool = False
    max_overflow: int = 30
    pool_size: int = 20
    pool_pre_ping: bool = True
    pool_recycle: int = 3600


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=".env",
        env_nested_delimiter="__",
        extra="ignore",
    )

    server: ServerConfig = ServerConfig()

    db: DatabaseConfig


settings = Settings()  # type: ignore
