"""
UserService contains the logic for handling user operations
"""
from bson import ObjectId
from src.models.users import User
from src.features.order_management.user_data_access import UserDataAccess


class UserService():
    """
    UserService is responsible for getting a user
    """
    def __init__(self):
        self.user_data_access = UserDataAccess()

    def get_user(self, user_id: ObjectId) -> User:
        """
        This function gets a user by id

        params:
            - user_id: the passed ID of the user
        """
        data = {"_id": user_id}
        user = self.user_data_access.get_user(data)
        return user
