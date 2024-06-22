from swagger_server.db.base import db


class PermissionContext(db.Model):
    __tablename__ = "permission_context"
