"""
This file contains authourization handling
"""
from bson import ObjectId
from fastapi import Depends, HTTPException
from src.middleware.jwt.auth import get_current_active_user
from src.models.users import Role, User
from src.config.database import roles_permissions, users_collection


def get_permission_dependency(permission: str) -> None:
    """
    This function checks if the user has the needed permission

    params:
        - permission: the permission to check for user
    """
    async def permission_dependency(current_user: User = Depends(get_current_active_user)):
        user = users_collection.find_one({"_id": ObjectId(current_user)})
        role_data = await _get_role(user.get("role"))
        if permission in role_data.get("permissions"):
            return
        raise HTTPException(
            status_code=403,
            detail="Operation not permitted"
        )
    return permission_dependency

async def _get_role(role_name: str) -> Role:
    """
    This function gets the Role class by role name

    params:
        - role_name: the role of the user
    """
    role = roles_permissions.find_one({"role": role_name})
    return role
