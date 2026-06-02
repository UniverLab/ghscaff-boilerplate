from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "{{name}}"
    debug: bool = False
    database_url: str = "sqlite:///./{{name}}.db"
    cors_origins: list[str] = ["http://localhost:5173"]

    model_config = {"env_prefix": "{{name}}_"}


settings = Settings()
