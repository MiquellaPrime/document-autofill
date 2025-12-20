from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class ServerConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=".env",
        env_nested_delimiter="__",
        extra="ignore",
    )

    server: ServerConfig = ServerConfig()


settings = Settings()  # type: ignore
