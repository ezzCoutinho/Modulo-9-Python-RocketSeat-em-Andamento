from typing import Dict

from src.controllers.interfaces.user_register_interface_controller import (
    UserRegisterInterfaceController,
)
from src.drivers.password_handler import PasswordHandler
from src.models.interfaces.user_repository_interface import UserRepositoryInterface


class UserRegister(UserRegisterInterfaceController):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository
        self.__password_handler = PasswordHandler()

    def registry(self, username: str, password: str) -> Dict:
        hashed_password = self.__create_hash_password(password)
        self.__registry_new_user(username, hashed_password)
        return self.__formatted_response(username)

    def __create_hash_password(self, password: str) -> str:
        hashed_password = self.__password_handler.encrypt_password(password)
        return hashed_password

    def __registry_new_user(self, username: str, hashed_password: str) -> None:
        self.__user_repository.registry_user(username, hashed_password)

    def __formatted_response(self, username: str) -> Dict:
        return {
            "type": "user",
            "count": 1,
            "username": username,
        }
