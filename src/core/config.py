from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "Marketplace"
    app_port: int = 8000
    debug: bool = False

    # Postgres settings
    postgres_user: str
    postgres_password: SecretStr
    postgres_db: str
    postgres_host: str
    postgres_port: int

    @property
    def postgres_url(self) -> str:
        password = self.postgres_password.get_secret_value()

        return (
            f"postgresql+asyncpg://{self.postgres_user}:{password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


settings = Settings()
