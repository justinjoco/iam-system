from swagger_server.db.base import db


class User(db.Model):
    __tablename__ = "user"
