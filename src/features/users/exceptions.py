"""
Exceptions for user feature
"""
from fastapi import HTTPException

class UserAlreadyExistsException(HTTPException):
    """
    UserAlreadyExistsException Exception
    """
    def __init__(self):
        super().__init__(status_code=409, detail="User already registered")

class InvalidUser(HTTPException):
    """
    InvalidUser Exception
    """
    def __init__(self):
        super().__init__(status_code=401, detail="Could not validate credentials")
