"""
UserDataAccess handles all operations related to user collection
"""
from src.config.database import users_collection
from src.models.users import User


class UserDataAccess():
    """
    UserDataAccess is responsible for getting a user
    """
    def get_user(self, data: dict) -> User:
        """
        This function gets one user from the db

        params:
            - data: contains filters to pass to the query
        """
        user = users_collection.find_one(data)
        return user
