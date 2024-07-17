"""
This file contains Order collection related items
"""
from enum import Enum
from pydantic import BaseModel

class OrderStatus(Enum):
    """
    Enums for stripe status related to the order
    """
    SUCCESS="SUCCESS"
    FAILED="FAILED"
    PENDING="PENDING"

class Orders(BaseModel):
    """
    The Orders Model
    """
    user_id: str
    products_list: list[dict]
    status: str
    client_secret_id: str

class OrdersHistory(BaseModel):
    """
    The OrdersHistory Model
    """
    order_id: str
    user_id: str
    products_list: list[dict]
    status: str
    client_secret_id: str
