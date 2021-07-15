from pydantic import BaseSettings


class Database(BaseSettings):
    host: str
    port: int
    username: str
    password: str
    name: str

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
