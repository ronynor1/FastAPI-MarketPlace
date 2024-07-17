"""
OrderDataAccess is the data access for order management
"""
from src.config.database import orders_collection
from src.models.orders import Orders


class OrderDataAccess():
    """
    OrderDataAccess is responsible for getting all orders and an order details
    """
    def get_orders(self, data: dict) -> list[Orders]:
        """
        This function gets several orders from the db

        params:
            - data: contains filters to pass to the query
        """
        orders = orders_collection.find(data)
        return orders

    def get_order_details(self, data: dict) -> Orders:
        """
        This function gets one order from the db

        params:
            - data: contains filters to pass to the query
        """
        order = orders_collection.find_one(data)
        return order
