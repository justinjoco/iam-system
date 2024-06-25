from swagger_server.db.base import AuditEntity
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID
from sqlalchemy.schema import FetchedValue
from sqlalchemy import ForeignKey


class User(AuditEntity):
    __tablename__ = "user"

    id: Mapped[UUID] = mapped_column(primary_key=True,
                                     nullable=False,
                                     server_default=FetchedValue())
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(nullable=False)
    manager_id: Mapped[UUID] = mapped_column()
    is_deactivated: Mapped[bool] = mapped_column(nullable=False,
                                                 server_default=FetchedValue())

    __mapper_args__ = {"polymorphic_identity": "user"}
