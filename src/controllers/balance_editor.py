from typing import Dict

from src.controllers.interfaces.balance_editor_interface_controller import (
    BalanceEditorInterfaceController,
)
from src.models.interfaces.user_repository_interface import UserRepositoryInterface


class BalanceEditor(BalanceEditorInterfaceController):
    def __init__(self, user_repository: UserRepositoryInterface):
        self.__user_repository = user_repository

    def edit(self, user_id: int, new_balance: float) -> Dict:
        self.__user_repository.edit_balance(user_id, new_balance)
        return {"type": "User", "count": 1, "new balance": new_balance}
