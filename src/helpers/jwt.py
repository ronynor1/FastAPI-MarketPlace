"""
This file contains functionalities related to the token
"""
import os
from datetime import timedelta, datetime
from jose import jwt

def create_access_token(data: dict, expires_delta: timedelta = None) -> dict:
    """
    This function creates the access token

    params:
        - data: the needed data to encode
        - expires_delta: the duration of the token
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return encoded_jwt
