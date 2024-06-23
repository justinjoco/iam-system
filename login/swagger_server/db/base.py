from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy.schema import FetchedValue


class Base(DeclarativeBase):
    pass


class AuditEntity(Base):
    __tablename__ = "audit_entity"

    # One field needs to be a 'primary key' in SQLALchemy even though this table in the DB does not actually have one
    date_created: Mapped[datetime] = mapped_column(
        primary_key=True,
        nullable=False,
        server_default=FetchedValue())
    date_updated: Mapped[datetime] = mapped_column(
        primary_key=True,
        nullable=False,
        server_default=FetchedValue())

    __mapper_args__ = {"polymorphic_identity": "audit_entity"}


db = SQLAlchemy(model_class=Base)
