from swagger_server.db.base import AuditEntity
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID
from sqlalchemy.schema import FetchedValue
from sqlalchemy import ForeignKey
from datetime import datetime
from typing import List


class RefreshToken(AuditEntity):
    __tablename__ = "refresh_token"

    id: Mapped[UUID] = mapped_column(primary_key=True,
                                     nullable=False,
                                     server_default=FetchedValue())
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"),
                                          nullable=False)
    expiry_date: Mapped[datetime] = mapped_column(nullable=False)
    scopes: Mapped[List[str]] = mapped_column(nullable=False,
                                              server_default=FetchedValue())
    is_expired: Mapped[bool] = mapped_column(nullable=False,
                                             server_default=FetchedValue())
    parent_id: Mapped[UUID] = mapped_column(ForeignKey("refresh_token.id"))

    __mapper_args__ = {"polymorphic_identity": "refresh_token"}
