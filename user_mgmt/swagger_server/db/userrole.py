from swagger_server.db.base import AuditEntity
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID
from sqlalchemy.schema import FetchedValue
from sqlalchemy import ForeignKey


class UserRole(AuditEntity):
    __tablename__ = "userrole"

    id: Mapped[UUID] = mapped_column(primary_key=True,
                                     nullable=False,
                                     server_default=FetchedValue())

    __mapper_args__ = {"polymorphic_identity": "user_role"}
