"""
OrderService is the service for order management
"""
from bson import ObjectId
from src.models.users import UserRole
from src.features.order_management.exceptions import InvalidOrder
from src.features.order_management.order_data_access import OrderDataAccess
from src.models.orders import Orders


class OrderService():
    """
    OrderService is responsible for getting all orders and an order details
    """
    def __init__(self):
        self.order_data_access = OrderDataAccess()

    def get_orders(self, user_id: ObjectId, role: str) -> list[Orders]:
        """
        This function gets orders based on the role of the user.
        The seller can see everything but the buyer can only his purchases

        params:
            - user_id: the logged in user
            - role: the role of the logged in user
        """
        data = {}
        if role == UserRole.BUYER.value:
            data = {"user_id": str(user_id)}
        orders = self.order_data_access.get_orders(data)
        return orders

    def get_order_details(self, order_id: ObjectId, user_id: ObjectId, role: str) -> Orders:
        """
        This function get the order details based on the role of the user.
        The seller can see it but the buyer can only his order

        params:
            - order_id: the chosen order
            - user_id: the logged in user
            - role: the role of the logged in user
        """
        data = {"_id": order_id}
        if role == UserRole.BUYER.value:
            data.update({"user_id": str(user_id)})
        order = self.order_data_access.get_order_details(data)
        if not order:
            raise InvalidOrder()
        return order
