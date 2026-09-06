from enum import Enum


class SellerStaffRole(Enum):
    """
    Staff roles enumeration designed for "seller_staff" table
    """

    OWNER = "owner"
    MANAGER = "manager"
    WAREHOUSE = "warehouse"
