"""
This file contains all functions related to password hashing and verification
"""
from passlib.context import CryptContext


def hash_password(password: str) -> str:
    """
    This function hashes the password given in the parameter

    params:
        - password: the provided password
    """
    hashed_password = None
    if isinstance(password, str) and len(password) > 0:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        hashed_password = pwd_context.hash(password)
    return hashed_password

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    This function verifies the plain password vs the hashed password by CryptContext

    params:
        - plain_password: the plain password
        - hashed_password: the hashed password
    """
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.verify(plain_password, hashed_password)
