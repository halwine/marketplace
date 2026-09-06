from uuid import UUID, uuid7

from sqlalchemy import Enum, ForeignKey, Index, String, UniqueConstraint, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import SellerStaffRole
from src.models.base import Base, SoftDeleteMixin, TimestampMixin


class Seller(SoftDeleteMixin, TimestampMixin, Base):
    """
    Seller class representing "sellers" table
    """

    __tablename__ = "sellers"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid7,
    )

    shop_name: Mapped[str] = mapped_column(
        String(125),
    )

    legal_name: Mapped[str] = mapped_column(
        String(125),
    )

    inn: Mapped[str] = mapped_column(
        String(12),
    )

    staff: Mapped[list["SellerStaff"]] = relationship(back_populates="seller")


class SellerStaff(TimestampMixin, Base):
    """
    SellerStaff represents "seller_staff" table
    """

    __tablename__ = "seller_staff"

    id: Mapped[int] = mapped_column(primary_key=True)

    seller_id: Mapped[UUID] = mapped_column(
        ForeignKey("sellers.id", ondelete="CASCADE"),
    )

    member_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
    )

    role: Mapped[SellerStaffRole] = mapped_column(
        Enum(
            SellerStaffRole,
            # Puts ENUM role value inside
            values_callable=lambda roles: [r.value for r in roles],
        ),
    )

    seller: Mapped["Seller"] = relationship(back_populates="staff")

    member: Mapped["User"] = relationship()  # noqa: F821

    __table_args__ = (
        UniqueConstraint("member_id", "seller_id"),
        Index(
            "uq_seller_staff_single_owner",
            "seller_id",
            unique=True,
            postgresql_where=text("role = 'owner'"),
        ),
    )
