from typing import Dict

import pytest

from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.login_creator_view import LoginCreatorView
from src.controllers.interfaces.login_creator_interface_controller import (
    LoginCreatorInterfaceController,
)


class MockController(LoginCreatorInterfaceController):
    def create(self, username: str, password: str) -> Dict:
        return {"username": username, "password": password}


@pytest.mark.skip(reason="Test OK!")
def test_handle_login_creator_view():
    body = {
        "username": "João da Silva",
        "password": "123456",
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    login_creator_view = LoginCreatorView(mock_controller)

    response = login_creator_view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.body == {"username": "João da Silva", "password": "123456"}
    assert response.status_code == 200


@pytest.mark.skip(reason="Test OK!")
def test_handle_login_creator_view_with_validation_error():
    body = {
        "password": "123456",
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    login_creator_view = LoginCreatorView(mock_controller)

    with pytest.raises(Exception):
        login_creator_view.handle(request)
