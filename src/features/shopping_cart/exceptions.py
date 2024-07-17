"""
Exceptions for shopping cart feature
"""
from fastapi import HTTPException

class EmptyCartException(HTTPException):
    """
    EmptyCartException Exception
    """
    def __init__(self):
        super().__init__(status_code=400, detail="Empty Cart!")
