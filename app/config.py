from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST", "PROD"] = "DEV"
    
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "name"
    DB_USER: str = "username"
    DB_PASS: str = "password"

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    TEST_DB_HOST: str = "localhost"
    TEST_DB_PORT: int = 5432
    TEST_DB_NAME: str = "name"
    TEST_DB_USER: str = "username"
    TEST_DB_PASS: str = "password"

    @property
    def test_database_url(self) -> str:
        return f"postgresql+asyncpg://{self.TEST_DB_USER}:{self.TEST_DB_PASS}@{self.TEST_DB_HOST}:{self.TEST_DB_PORT}/{self.TEST_DB_NAME}"
    
    
    
    
    SECRET_KEY: str =  "secret_key"
    ALGORITHM: str = "algorithm"
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    
settings = Settings()
