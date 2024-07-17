"""
This file contains all Product related items
"""
from typing import Union
from pydantic import BaseModel, constr

class Product(BaseModel):
    """
    The Product Model
    """
    name: Union[str, constr(min_length=1)]
    description: Union[str, constr(min_length=1)]
    price: int
    images: Union[str, constr(min_length=1)]
