from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # --- ROUTERS ---
    ROUTER_PREFIX: str = 'api_'
    ROUTER_RESPONSE: str = ROUTER_PREFIX + 'responses'

    # --- KAFKA ---
    KAFKA_HOST: str = 'localhost'
    KAFKA_PORT: int = 9092

    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()
