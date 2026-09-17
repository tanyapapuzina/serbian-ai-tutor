from functools import lru_cache

from pydantic import Field  # Field позволяет настроить отдельное поле
from pydantic_settings import BaseSettings, SettingsConfigDict

# BaseSettings — специальный класс Pydantic для чтения настроек из environment variables.
# SettingsConfigDict — конфигурация поведения settings-класса.

class Settings(BaseSettings):
    telegram_bot_token: str = Field(alias="TELEGRAM_BOT_TOKEN")
    database_url: str = Field(alias="DATABASE_URL")
    openrouter_api_key: str = Field(alias="OPENROUTER_API_KEY")
    llm_model: str = Field(default="openrouter/free", alias="LLM_MODEL")
    app_env: str = Field(default="development", alias="APP_ENV")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

# lru_cache — декоратор из стандартной библиотеки Python.
# Он запоминает результат функции. Без него каждый вызов get_settings 
# создавал бы новый объект Settings и заново читал env.

@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]