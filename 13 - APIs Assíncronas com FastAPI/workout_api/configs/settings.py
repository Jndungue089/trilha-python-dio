from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = Field(default='postgresql+asyncpg://postgres:root@localhost:5432/workout')
    

settings = Settings()