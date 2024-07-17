"""
UserContoller is the controller for user operations
"""
from src.features.users.user_service import UserService
from src.features.users.validation_service import ValidationService
from src.models.users import User


class UserContoller():
    """
    UserContoller handles registration and login of the user
    """
    def __init__(self):
        self.validation_service = ValidationService()
        self.user_service = UserService()

    def register_user(self, user: User) -> None:
        """
        This function registers the user

        params:
            - user: User db model
        """
        self.validation_service.check_user_exists(user.email)
        self.user_service.add_user(user)

    def login_user(self, email: str, password: str) -> dict:
        """
        This function gives permission for the user to login

        params:
            - email: the email in the request body
            - password: the password in the request body
        """
        user = self.user_service.get_user(email)
        self.validation_service.verify_user(user, password)
        response = self.user_service.get_token(user.get("email"))
        return response
