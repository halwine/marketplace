from uuid import UUID, uuid7

from src.models.base import Base, TimestampMixin
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid7,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
    )

    phone_number: Mapped[str | None] = mapped_column(
        String(20),
        unique=True,
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255),
    )

    name: Mapped[str] = mapped_column(
        String(50),
    )

    last_name: Mapped[str] = mapped_column(
        String(50),
    )

    is_admin: Mapped[bool] = mapped_column(
        default=False,
    )
