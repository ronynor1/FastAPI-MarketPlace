"""
OrderController is the controller for order management
"""
from bson import ObjectId
from src.features.order_management.order_service import OrderService
from src.features.order_management.user_service import UserService
from src.schema.orders_schema import order_serialize, orders_list


class OrderContoller():
    """
    OrderContoller is responsible for getting all orders and an order details
    """
    def __init__(self):
        self.order_service = OrderService()
        self.user_service = UserService()

    def get_orders(self, user_id: ObjectId) -> list[dict]:
        """
        This function gets the user and, based on their role, orders will be retrieved

        params:
            - user_id: the logged in user
        """
        user = self.user_service.get_user(user_id)
        orders = self.order_service.get_orders(user_id, user.get("role"))
        response = orders_list(orders)
        return response

    def get_order_details(self, order_id: ObjectId, user_id: ObjectId) -> dict:
        """
        This function gets the user and, based on their role, the order details will be retrieved by id

        params:
            - order_id: the chosen order
            - user_id: the logged in user
        """
        user = self.user_service.get_user(user_id)
        order = self.order_service.get_order_details(order_id, user_id, user.get("role"))
        response = order_serialize(order)
        return response
