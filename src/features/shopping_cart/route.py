"""
The main route for shopping cart
"""
from bson import ObjectId
from fastapi import APIRouter, Depends, Header, Request
from src.features.shopping_cart.shopping_controller import ShoppingController
from src.middleware.jwt.auth import get_current_user
from src.middleware.authorization.permission import get_permission_dependency
from src.features.shopping_cart.request_models import CheckoutRequestModel

shopping_router = APIRouter()

@shopping_router.post("/checkout", dependencies=[Depends(get_permission_dependency("checkout"))])
async def checkout(body: CheckoutRequestModel, current_user: ObjectId = Depends(get_current_user)):
    """
    Checkout and pay for the purchased products
    """
    shopping_controller = ShoppingController()
    shopping_controller.checkout(current_user, body.products_list)
    return {"message":"Order Submitted"}

@shopping_router.post("/webhook")
async def webhook_received(request: Request, stripe_signature: str = Header(str)):
    """
    This is the webhook for receiving the response of the stripe integration
    """
    data = await request.body()
    shopping_controller = ShoppingController()
    shopping_controller.handle_webhook(data, stripe_signature)
