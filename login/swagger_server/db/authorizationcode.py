from swagger_server.db.base import db


class AuthorizationCode(db.Model):
    __tablename__ = "authorization_code"
