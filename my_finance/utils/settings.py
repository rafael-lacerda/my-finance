from typing import Dict

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"

    USERS: Dict = Field(default={"user": "password"})
    SECRET_KEY: str = Field(default="secret_key")

    DATABASE_HOST: str = Field(default="localhost")
    DATABASE_PORT: int = Field(default=5432)
    DATABASE_NAME: str = Field(default="my_finance")
    DATABASE_USER: str = Field(default="my_finance_user")
    DATABASE_PASSWORD: str = Field(default="my_finance_password")
