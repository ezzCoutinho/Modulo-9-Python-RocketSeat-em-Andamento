from src.controllers.interfaces.balance_editor_interface_controller import (
    BalanceEditorInterfaceController,
)
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class BalanceEditorView(ViewInterface):
    def __init__(self, controller: BalanceEditorInterfaceController) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        new_balance = http_request.body.get("new_balance")
        user_id = http_request.param.get("user_id")

        self.__validate_inputs(user_id, new_balance)
        response = self.__controller.edit(user_id, new_balance)
        return HttpResponse(status_code=200, body=response)

    def __validate_inputs(self, user_id: any, new_balance: any) -> None:
        if not user_id or not new_balance or not isinstance(new_balance, float):
            raise Exception("Invalid Input")
