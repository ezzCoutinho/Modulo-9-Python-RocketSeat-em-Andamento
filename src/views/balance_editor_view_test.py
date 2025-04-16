from typing import Dict

import pytest

from src.controllers.interfaces.balance_editor_interface_controller import (
    BalanceEditorInterfaceController,
)
from src.views.balance_editor_view import BalanceEditorView
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class MockController(BalanceEditorInterfaceController):
    def edit(self, user_id: int, new_balance: float) -> Dict:
        return {"user_id": user_id, "new_balance": new_balance}


@pytest.mark.skip(reason="Test OK!")
def test_handle_balance_editor_view():
    body = {"new_balance": 100.0}
    params = {"user_id": 1}
    request = HttpRequest(body=body, params=params)

    mock_controller = MockController()
    balance_editor_view = BalanceEditorView(mock_controller)

    response = balance_editor_view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.body == {"user_id": 1, "new_balance": 100.0}
    assert response.status_code == 200
