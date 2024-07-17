"""
This file contains the schema for the users
"""
from bson import ObjectId
from src.models.users import User


def user_serialize(user: User) -> dict:
    """
    This function serializes the Users Model

    params:
        - user: the provided user
    """
    return {
        "id": ObjectId(user["_id"]),
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "email": user["email"],
        "password": user["password"],
        "role": user["role"],
    }
