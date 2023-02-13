from pydantic import BaseSettings

class Settings(BaseSettings):
    MSSQL_CONN:str  # default value if env variable does not exist

    class Config:
        env_file = ".env"