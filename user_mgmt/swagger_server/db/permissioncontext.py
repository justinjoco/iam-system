from swagger_server.db.base import AuditEntity
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID
from sqlalchemy.schema import FetchedValue
from sqlalchemy import ForeignKey


class PermissionContext(AuditEntity):
    __tablename__ = "permission_context"

    id: Mapped[UUID] = mapped_column(primary_key=True,
                                     nullable=False,
                                     server_default=FetchedValue())
    permission_id: Mapped[UUID] = mapped_column(ForeignKey("permission.id"),
                                                nullable=False)
    resource_id: Mapped[UUID] = mapped_column(nullable=False)

    __mapper_args__ = {"polymorphic_identity": "permission_context"}
