"""
This file contains the schema for the orders
"""
from src.models.products import Product


def product_serialize(product: Product) -> dict:
    """
    This function serializes the Product Model

    params:
        - product: the provided product
    """
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "description": product["description"],
        "price": product["price"],
        "image": product["image"],
    }

def products_list(products: list[Product]) -> list[dict]:
    """
    This function serializes the Product Model that is in a list

    params:
        - products: the provided list of products
    """
    return [product_serialize(product) for product in products]
