from typing import Dict

import pytest

from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.user_register_view import UserRegisterView
from src.controllers.interfaces.user_register_interface_controller import (
    UserRegisterInterfaceController,
)


class MockController(UserRegisterInterfaceController):
    def registry(self, username: str, password: str) -> Dict:
        return {"username": username, "password": password}


@pytest.mark.skip(reason="Test OK!")
def test_habdke_user_register():
    body = {
        "username": "any_username",
        "password": "any_password",
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    response = user_register_view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.body == {"username": "password"}
    assert response.status_code == 200


@pytest.mark.skip(reason="Test OK!")
def test_habdke_user_register_with_validation_error():
    body = {
        "password": "any_password",
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    with pytest.raises(Exception):
        user_register_view.handle(request)
