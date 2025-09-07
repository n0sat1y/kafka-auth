from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # --- ROUTERS ---
    ROUTER_PREFIX: str = 'auth_'
    ROUTER_RESPONSE: str = ROUTER_PREFIX + 'responses'

    # --- KAFKA ---
    KAFKA_HOST: str = 'localhost'
    KAFKA_PORT: int = 9092
    
    #--- JWT ---
    SECRET_KEY: str = 'sdfglbhnslfs3454Gb87gI87'
    JWT_ALGORITHM: str = 'HS256'
    JWT_ACCESS_LIFESPAN_MINUTES: int = 15
    JWT_REFRESH_LIFESPAN_DAYS: int = 10

    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()
