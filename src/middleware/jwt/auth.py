"""
This file handles user verification by jwt
"""
from fastapi import Depends, HTTPException
from src.schema.user_schema import user_serialize
from src.config.database import users_collection
from src.middleware.jwt.jwt_bearer import JWTBearer
from src.middleware.jwt.jwt_handler import decode_jwt
from src.models.users import User


async def get_current_user(token: str = Depends(JWTBearer())):
    """
    This function gets the user from the token

    params:
        - token: normally the token of the logged in user
    """
    payload = decode_jwt(token)
    username = payload.get("sub")
    if username is None:
        raise HTTPException(status_code=403, detail="Could not validate credentials")
    user = users_collection.find_one({"email": username})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user = user_serialize(user)
    return user.get("id")

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    """
    This function of gets the current user

    params:
        - current_user: the active user
    """
    return current_user
