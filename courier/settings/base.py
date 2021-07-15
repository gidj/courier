from pydantic import BaseSettings


class Database(BaseSettings):
    host: str = "localhost"
    port: int = 5432
    username: str = "admin"
    password: str = ""
    name: str = "courier"

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        _uri = "postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}"
        return _uri.format(
            username=self.username,
            password=self.password,
            host=self.host,
            port=self.port,
            name=self.name,
        )