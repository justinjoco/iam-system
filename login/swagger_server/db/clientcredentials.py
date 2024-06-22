from swagger_server.db.base import db


class ClientCredentials(db.Model):
    __tablename__ = "client_credentials"
