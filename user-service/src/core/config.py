from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # --- KAFKA ---
    KAFKA_HOST: str = 'localhost'
    KAFKA_PORT: int = 9092

    #--- DB ---
    POSTGRES_USER: str = 'user'
    POSTGRES_PASSWORD: str = 'password'
    POSTGRES_DB: str = 'db'
    POSTGRES_HOST: str = 'localhost'
    POSTGRES_PORT: int = 5433

    @property
    def POSTGRES_URL(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(env_file='.env')
    

settings = Settings()
