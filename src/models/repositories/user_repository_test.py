from unittest.mock import Mock

from src.models.repositories.user_repository import UserRepository


class MockCursor:
    def __init__(self):
        self.execute = Mock()
        self.fetchone = Mock()


class MockConnection:
    def __init__(self):
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()


def test_repository():
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
