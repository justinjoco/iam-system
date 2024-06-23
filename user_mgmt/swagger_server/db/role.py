from swagger_server.db.base import AuditEntity
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID
from sqlalchemy.schema import FetchedValue
from sqlalchemy import ForeignKey


class Role(AuditEntity):
    __tablename__ = "role"

    id: Mapped[UUID] = mapped_column(primary_key=True,
                                     nullable=False,
                                     server_default=FetchedValue())
    name: Mapped[str] = mapped_column(nullable=False)

    __mapper_args__ = {"polymorphic_identity": "role"}
