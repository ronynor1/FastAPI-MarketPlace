"""
Request models for the shopping cart feature
"""
from pydantic import BaseModel

class CheckoutRequestModel(BaseModel):
    """
    CheckoutRequestModel is the body of the checkout POST API

    body:
        - products_list: contains all the IDs of the bought products
    """
    products_list: list[str]
