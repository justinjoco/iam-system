from swagger_server.db.base import AuditEntity
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID
from sqlalchemy.schema import FetchedValue
from sqlalchemy import ForeignKey


class ClientCredentials(AuditEntity):
    __tablename__ = "client_credentials"

    id: Mapped[UUID] = mapped_column(primary_key=True, nullable=False)
    salted_secret_hash: Mapped[str] = mapped_column(nullable=False)
    salt: Mapped[str] = mapped_column(nullable=False)

    __mapper_args__ = {"polymorphic_identity": "client_credentials"}
