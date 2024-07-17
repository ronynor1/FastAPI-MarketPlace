"""
The main route for user operations
"""
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from src.models.users import User
from src.features.users.user_controller import UserContoller
users_router = APIRouter()

@users_router.post("/register")
async def register_user(user: User):
    """
    Register a user
    """
    user_controller = UserContoller()
    user_controller.register_user(user)
    return {"message":"User successfully registered"}

@users_router.post("/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    User Login returning a token
    """
    user_controller = UserContoller()
    response = user_controller.login_user(form_data.username, form_data.password)
    return response
