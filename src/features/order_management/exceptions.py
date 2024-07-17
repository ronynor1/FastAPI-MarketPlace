"""
Exceptions for order management feature
"""
from fastapi import HTTPException

class InvalidOrder(HTTPException):
    """
    InvalidOrder Exception
    """
    def __init__(self):
        super().__init__(status_code=404, detail="Order not found")
