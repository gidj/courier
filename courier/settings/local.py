from . import base


class Database(base.Database):
    ...

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return "sqlite:///:memory:"
