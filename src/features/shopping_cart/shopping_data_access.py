"""
ShoppingDataAccess is the data access for shopping cart
"""
from bson import ObjectId
from src.config.database import products_collection, orders_collection, orders_history_collection
from src.models.products import Product
from src.models.orders import OrderStatus, Orders, OrdersHistory


class ShoppingDataAccess():
    """
    ShoppingDataAccess is responsible for getting all products, insert and update orders and orders history
    """
    def get_products(self, products_ids: list[ObjectId]) -> list[Product]:
        """
        This function gets products filtered by array of IDs

        params:
            - products_ids: the purchased products
        """
        products = products_collection.find({
            '_id': {'$in': products_ids}
        })
        return list(products)

    def insert_order(self, user_id: ObjectId, products: list[dict], client_secret_id: str) -> None:
        """
        This function creates an order and add the order to the history

        params:
            - user_id: the logged in user
            - products: the purchased products
            - client_secret_id: reference id created by stripe
        """
        order = Orders(
            user_id=str(user_id),
            products_list=products,
            status=OrderStatus.PENDING.value,
            client_secret_id=client_secret_id
        )
        order = orders_collection.insert_one(dict(order))

        order_history = OrdersHistory(
            order_id=str(order.inserted_id),
            user_id=str(user_id),
            products_list=products,
            status=OrderStatus.PENDING.value,
            client_secret_id=client_secret_id
        )
        orders_history_collection.insert_one(dict(order_history))

    def update_order_status(self, client_secret_id: str, status: str) -> None:
        """
        This function updates the order and add the order to the history

        params:
            - client_secret_id: reference id created by stripe
            - status: SUCCESS, FAILED
        """
        filter_criteria = {'client_secret_id': client_secret_id}
        update_data = {'$set': {'status': status}}
        orders_collection.update_one(filter_criteria, update_data)

        data = {"client_secret_id": client_secret_id}
        order = orders_collection.find_one(data)
        order_history = OrdersHistory(
            order_id=str(order.get("_id")),
            user_id=str(order.get("user_id")),
            products_list=order.get("products_list"),
            status=status,
            client_secret_id=client_secret_id
        )
        orders_history_collection.insert_one(dict(order_history))
