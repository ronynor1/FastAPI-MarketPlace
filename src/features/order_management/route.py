"""
The main route for order management
"""
from bson import ObjectId
from fastapi import APIRouter, Depends
from src.middleware.authorization.permission import get_permission_dependency
from src.middleware.jwt.auth import get_current_user
from src.features.order_management.order_controller import OrderContoller

orders_router = APIRouter()

@orders_router.get("/orders", dependencies=[Depends(get_permission_dependency("get_orders"))])
async def get_orders(user_id: ObjectId = Depends(get_current_user)):
    """
    Fetch all orders based on user_id and other conditions
    """
    order_controller = OrderContoller()
    response = order_controller.get_orders(user_id)
    return response

@orders_router.get("/orders/{order_id}", dependencies=[Depends(get_permission_dependency("get_order_details"))])
async def get_order_details(order_id: str, user_id: ObjectId = Depends(get_current_user)):
    """
    Fetch order details based on order_id, user_id and other conditions
    """
    order_controller = OrderContoller()
    response = order_controller.get_order_details(ObjectId(order_id), user_id)
    return response
