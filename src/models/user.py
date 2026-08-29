from datetime import datetime
from uuid import UUID, uuid7

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base, TimestampMixin


class User(TimestampMixin, Base):
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

    addresses: Mapped[list[UserAddress]] = relationship(back_populates="user")


class UserAddress(Base, TimestampMixin):
    __tablename__ = "user_addresses"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
    )

    city: Mapped[str] = mapped_column(
        String(30),
    )

    street: Mapped[str] = mapped_column(
        String(100),
    )

    house: Mapped[str] = mapped_column(
        String(10),
    )

    apartment: Mapped[str | None] = mapped_column(
        String(10),
    )

    last_used_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
    )

    user: Mapped[User] = relationship(back_populates="addresses")
