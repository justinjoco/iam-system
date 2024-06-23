from swagger_server.db.base import AuditEntity
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID
from datetime import datetime
from sqlalchemy.schema import FetchedValue
from sqlalchemy import ForeignKey


class AuthorizationCode(AuditEntity):
    __tablename__ = "authorization_code"

    id: Mapped[UUID] = mapped_column(primary_key=True,
                                     nullable=False,
                                     server_default=FetchedValue())

    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"),
                                          nullable=False)
    expiry_date: Mapped[datetime] = mapped_column(nullable=False)
    code_challenge: Mapped[str] = mapped_column(nullable=False)
    code_challenge_method: Mapped[str] = mapped_column(nullable=False)

    __mapper_args__ = {"polymorphic_identity": "authorization_code"}
