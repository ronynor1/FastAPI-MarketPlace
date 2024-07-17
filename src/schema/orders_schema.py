"""
This file contains the schema for the orders
"""
from src.models.orders import Orders
from src.schema.products_schema import products_list


def order_serialize(order: Orders) -> dict:
    """
    This function serializes the Orders Model

    params:
        - order: the provided order
    """
    return {
        "id": str(order["_id"]),
        "user_id": order["user_id"],
        "products_list": products_list(order["products_list"]),
        "status": order["status"],
        "client_secret_id": order["client_secret_id"],
    }

def orders_list(orders: list[Orders]) -> list[dict]:
    """
    This function serializes the Orders Model that is in a list

    params:
        - orders: the provided list of orders
    """
    return [order_serialize(order) for order in orders]
