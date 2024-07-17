"""
UserService is the service for user operations
"""
from datetime import timedelta
from src.helpers.hash import hash_password
from src.helpers.jwt import create_access_token
from src.models.users import User
from src.features.users.user_data_access import UserDataAccess

ACCESS_TOKEN_EXPIRE_MINUTES = 120

class UserService():
    """
    UserService gets and add a user, and gets the access token
    """
    def __init__(self):
        self.user_data_access = UserDataAccess()

    def add_user(self, user: User) -> None:
        """
        This function adds a user to the db

        params:
            - user: User db model
        """
        hashed_password = hash_password(user.password)
        user.password = hashed_password
        self.user_data_access.add_user(user)

    def get_user(self, email: str) -> User:
        """
        This function gets one user from the db

        params:
            - email: gets the user by the email
        """
        data = {"email": email}
        user = self.user_data_access.get_user(data)
        return user

    def get_token(self, email: str) -> dict:
        """
        This function gets the access token

        params:
            - email: the value is stored in the access token
        """
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"sub": email}, expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}
