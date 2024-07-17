"""
StripeIntegration class handles everything related to the stripe integration
"""
import os
from typing import Union
import stripe
from src.models.orders import OrderStatus


class StripeIntegration():
    """
    StripeIntegration creates payment intent and handles the webhook behavior
    """
    def __init__(self):
        stripe.api_key = os.getenv("STRIPE_API_KEY")

    def create_payment_intent(self, total_price: int) -> None:
        """
        This function initiates the payment for stripe

        params:
            - total_price: the price that the use needs to pay
        """
        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=total_price*100,
                currency="usd",
                automatic_payment_methods={
                    "enabled": True,
                    "allow_redirects": "never"
                },
                confirm=True,
                payment_method="pm_card_visa"
            )
            return payment_intent.client_secret
        except stripe.error.StripeError as e:
            return {"error": str(e)}

    def handle_webhook(self, data: dict, stripe_signature: str) -> Union[tuple[str,str], None]:
        """
        This function handles the webhook communication for stripe

        params:
            - data: the data of the payment intent
            - stripe_signature: the signature header
        """
        webhook_secret = os.getenv("WEBHOOK_API_KEY")
        try:
            event = stripe.Webhook.construct_event(
                payload=data,
                sig_header=stripe_signature,
                secret=webhook_secret
            )
            if event["type"] == "payment_intent.succeeded":
                payment_intent = event.data.object
                return payment_intent.get("client_secret"), OrderStatus.SUCCESS.value
            elif event["type"] == "payment_intent.payment_failed":
                payment_intent = event.data.object
                return payment_intent.get("client_secret"), OrderStatus.FAILED.value
        except Exception as e:
            return {"error": str(e)}
