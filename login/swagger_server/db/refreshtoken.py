from swagger_server.db.base import db


class RefreshToken(db.Model):
    __tablename__ = "refresh_token"
