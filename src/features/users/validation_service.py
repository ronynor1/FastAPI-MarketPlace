"""
ValidationService is responsible for the user operations
"""
from typing import Union
from src.features.users.exceptions import InvalidUser, UserAlreadyExistsException
from src.features.users.user_data_access import UserDataAccess
from src.helpers.hash import verify_password
from src.models.users import User


class ValidationService():
    """
    ValidationService checks if user exists and verify user password
    """
    def __init__(self):
        self.user_data_access = UserDataAccess()

    def check_user_exists(self, email: str) -> None:
        """
        This function checks if the user exists in the db

        params:
            - emails: email of the user
        """
        data = {"email": email}
        user = self.user_data_access.get_user(data)
        if user:
            raise UserAlreadyExistsException()

    def verify_user(self, user: Union[User, None], password: str) -> None:
        """
        This function verifies the credibility of the user

        params:
            - user: db user
            - password: entered password
        """
        if not user or not verify_password(password, user.get("password")):
            raise InvalidUser()
