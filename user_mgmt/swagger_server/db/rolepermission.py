from swagger_server.db.base import AuditEntity
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID
from sqlalchemy.schema import FetchedValue
from sqlalchemy import ForeignKey


class RolePermission(AuditEntity):
    __tablename__ = "role_permission"

    id: Mapped[UUID] = mapped_column(primary_key=True,
                                     nullable=False,
                                     server_default=FetchedValue())
    role_id: Mapped[UUID] = mapped_column(ForeignKey("role.id"),
                                          nullable=False)
    permission_id: Mapped[UUID] = mapped_column(ForeignKey("permission.id",
                                                           nullable=False))

    __mapper_args__ = {"polymorphic_identity": "role_permission"}
