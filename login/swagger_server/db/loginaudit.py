from swagger_server.db.base import db


class LoginAudit(db.Model):
    __tablename__ = "login_audit"
