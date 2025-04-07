from unittest.mock import Mock

import pytest

from src.models.repositories.user_repository import UserRepository


class MockCursor:
    def __init__(self):
        self.execute = Mock()
        self.fetchone = Mock()


class MockConnection:
    def __init__(self):
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()


@pytest.mark.skip(reason="Test OK!")
def test_registry_user():
    username = "Fred"
    password = "password"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.registry_user(username, password)

    cursor = mock_connection.cursor.return_value
    print(cursor)
    print(cursor.execute.call_args[0])

    assert "INSERT INTO users" in cursor.execute.call_args[0][0]
    assert "(username, password, balance)" in cursor.execute.call_args[0][0]
    assert "VALUES" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username, password, 0)


@pytest.mark.skip(reason="Test OK!")
def test_edit_balance():
    user_id = 1
    new_balance = 100.0

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.edit_balance(user_id, new_balance)

    cursor = mock_connection.cursor.return_value
    assert "UPDATE users" in cursor.execute.call_args[0][0]
    assert "SET balance = ?" in cursor.execute.call_args[0][0]
    assert "WHERE id = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (new_balance, user_id)

    mock_connection.commit.assert_called_once()


@pytest.mark.skip(reason="Test OK!")
def test_get_user_by_username():
    username = "Fred"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.get_user_by_username(username)

    cursor = mock_connection.cursor.return_value
    assert "SELECT id, username, password" in cursor.execute.call_args[0][0]
    assert "FROM users" in cursor.execute.call_args[0][0]
    assert "WHERE username = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username,)

    cursor.fetchone.assert_called_once()
