from swagger_server.db.base import AuditEntity
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID
from sqlalchemy.schema import FetchedValue
from sqlalchemy import ForeignKey


class LoginAudit(AuditEntity):
    __tablename__ = "login_audit"

    id: Mapped[UUID] = mapped_column(primary_key=True,
                                     nullable=False,
                                     server_default=FetchedValue())
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"),
                                          nullable=False)

    __mapper_args__ = {"polymorphic_identity": "login_audit"}
