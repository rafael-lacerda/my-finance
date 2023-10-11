from typing import Dict

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"

    SECRET_KEY: str = Field(default="secret_key")
