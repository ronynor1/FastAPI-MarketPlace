"""
ShoppingController is the controller for shopping cart
"""
from bson import ObjectId
from src.features.shopping_cart.exceptions import EmptyCartException
from src.integrations.stripe import StripeIntegration
from src.features.shopping_cart.shopping_service import ShoppingService


class ShoppingController():
    """
    ShoppingController is responsible for the checkout and webhook functionalities
    """
    def __init__(self):
        self.shopping_service = ShoppingService()
        self.stripe_client = StripeIntegration()

    def checkout(self, user_id: ObjectId, products: list[str]) -> None:
        """
        This function calculates the total price, calls the stripe integration to pay and creates order

        params:
            - user_id: the logged in user
            - products: the purchased products
        """
        if products:
            all_products = self.shopping_service.get_products(products)
            total_price = self.shopping_service.get_total_price(all_products)
            client_secret_id = self.stripe_client.create_payment_intent(total_price)
            self.shopping_service.insert_order(user_id, all_products, client_secret_id)
        else:
            raise EmptyCartException()

    def handle_webhook(self, data: dict, stripe_signature: str) -> None:
        """
        This function catches the stripe response and update db accordingly
        """
        result = self.stripe_client.handle_webhook(data, stripe_signature)
        if result:
            client_secret_id, status = result
            self.shopping_service.update_order_status(client_secret_id, status)
