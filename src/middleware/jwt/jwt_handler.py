"""
This file hadnles jwt veification and decoding
"""
import os
import jwt
from jwt import PyJWTError

def verify_jwt(jwtoken: str) -> bool:
    """
    This function verifies the token

    params:
        - jwtoken: the provided token
    """
    isTokenValid: bool = False
    try:
        payload = jwt.decode(jwtoken, os.getenv("SECRET_KEY"), algorithms=["HS256"])
    except PyJWTError:
        payload = None
    if payload:
        isTokenValid = True
    return isTokenValid

def decode_jwt(token: str):
    """
    This function decode the token

    params:
        - token: the provided token
    """
    try:
        decoded_token = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
        return decoded_token if decoded_token else None
    except PyJWTError:
        return {}
