from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # --- KAFKA ---
    KAFKA_HOST: str = 'localhost'
    KAFKA_PORT: int = 9092

    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()
