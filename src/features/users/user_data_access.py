"""
UserDataAccess is the data access for user operations
"""
from src.config.database import users_collection
from src.models.users import User


class UserDataAccess():
    """
    UserDataAccess gets and add a user
    """
    def get_user(self, data: dict) -> User:
        """
        This function gets one user from the db

        params:
            - data: contains filters to pass to the query
        """
        user = users_collection.find_one(data)
        return user

    def add_user(self, user: User) -> None:
        """
        This function adds a user to the db

        params:
            - user: User db model
        """
        users_collection.insert_one(dict(user))
