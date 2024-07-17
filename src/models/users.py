"""
This file contains Users collection related items
"""
from enum import Enum
from typing import Union
from pydantic import BaseModel, EmailStr, constr, validator

class UserRole(Enum):
    """
    Enum for all the roles of the user
    """
    BUYER="buyer"
    SELLER="seller"

class User(BaseModel):
    """
    The User Model
    """
    first_name: Union[str, constr(min_length=1)]
    last_name: Union[str, constr(min_length=1)]
    email: EmailStr
    password: Union[str, constr(min_length=1)]
    role: str

    @validator('role', pre=True, always=True)
    def validate_role(cls, value):
        if value not in [UserRole.BUYER.value, UserRole.SELLER.value]:
            raise ValueError(f'Invalid role: {value}')
        return value

class Role(BaseModel):
    """
    The Role Model
    """
    role: str
    permissions: list[str]
