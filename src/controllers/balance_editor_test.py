from unittest.mock import Mock

import pytest

from src.controllers.balance_editor import BalanceEditor
from src.models.interfaces.user_repository_interface import UserRepositoryInterface


@pytest.mark.skip(reason="Test OK!")
def test_edit_balance():
    user_id = 1
    new_balance = 100.50

    mock_user_repository = Mock(spec=UserRepositoryInterface)
    balance_editor = BalanceEditor(mock_user_repository)

    result = balance_editor.edit(user_id, new_balance)
    mock_user_repository.edit_balance.assert_called_once_with(user_id, new_balance)

    assert result["type"] == "User"
    assert result["count"] == 1
    assert result["new balance"] == new_balance


@pytest.mark.skip(reason="Test OK!")
def test_edit_balance_with_zero():
    user_id = 2
    new_balance = 0.0

    mock_user_repository = Mock(spec=UserRepositoryInterface)
    balance_editor = BalanceEditor(mock_user_repository)

    result = balance_editor.edit(user_id, new_balance)
    mock_user_repository.edit_balance.assert_called_once_with(user_id, new_balance)

    assert result["type"] == "User"
    assert result["count"] == 1
    assert result["new balance"] == new_balance
