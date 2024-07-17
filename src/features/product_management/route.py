"""
The main route for product management
"""
from bson import ObjectId
from fastapi import APIRouter, Depends
from src.middleware.authorization.permission import get_permission_dependency
from src.middleware.jwt.auth import get_current_user
from src.features.product_management.product_controller import ProductContoller

products_router = APIRouter()

@products_router.get("/products", dependencies=[Depends(get_permission_dependency("get_products"))])
async def get_products(user_id: ObjectId = Depends(get_current_user)):
    """
    Fetch all products
    """
    product_controller = ProductContoller()
    response = product_controller.get_products()
    return response

@products_router.get("/products/{product_id}", dependencies=[Depends(get_permission_dependency("get_product_details"))])
async def get_product_details(product_id: str, user_id: ObjectId = Depends(get_current_user)):
    """
    Fetch product details based on product_id
    """
    product_controller = ProductContoller()
    response = product_controller.get_product_details(ObjectId(product_id))
    return response
