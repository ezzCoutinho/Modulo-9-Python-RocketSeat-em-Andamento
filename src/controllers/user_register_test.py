import pytest

from src.controllers.user_register import UserRegister


class MockUserRepository:
    def __init__(self) -> None:
        self.registry_user_attributes = {}

    def registry_user(self, username: str, password: str) -> None:
        self.registry_user_attributes["username"] = username
        self.registry_user_attributes["password"] = password


@pytest.mark.skip(reason="Test OK!")
def test_registry():
    repository = MockUserRepository()
    controller = UserRegister(repository)  # type: ignore

    username = "Ola Mundo"
    password = "123456"

    response = controller.registry(username, password)

    assert response["type"] == "user"
    assert response["username"] == username

    assert repository.registry_user_attributes["username"] == username
    assert repository.registry_user_attributes["password"] is not None
    assert repository.registry_user_attributes["password"] != password
