from . import base


class Database(base.Database):
    host = "localhost"
    port = 5432
    username = "admin"
    password = ""
    name = "courier"
