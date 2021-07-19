from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USERNAME: str = "courier"
    DB_PASSWORD: str = "password"
    DB_NAME: str = "courier"

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        _uri = "postgresql+psycopg2://{username}:{password}@{host}:{port}/{name}"
        return _uri.format(
            username=self.DB_USERNAME,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            name=self.DB_NAME,
        )

    SQS_ENDPOINT_URL: Optional[str] = "http://aws:4566"
    SQS_REGION_NAME: Optional[str] = None

    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
