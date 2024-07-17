"""
Exceptions for product management feature
"""
from fastapi import HTTPException

class InvalidProduct(HTTPException):
    """
    InvalidProduct Exception
    """
    def __init__(self):
        super().__init__(status_code=404, detail="Product not found")
