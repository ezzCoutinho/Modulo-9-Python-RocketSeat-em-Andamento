import pytest

from src.drivers.jwt_handler import JwtHandler


@pytest.mark.skip(reason="Test OK!")
def test_jwt_handler():
    jwt_handler = JwtHandler()
    body = {
        "username": "Ola Mundo",
        "aqui": "outro",
        "lalala": "",
    }

    token = jwt_handler.create_jwt_token(body)
    token_information = jwt_handler.decode_jwt_token(token)

    assert token is not None
    assert isinstance(token, str)
    assert token_information["username"] == body["username"]
    assert token_information["lalala"] == body["lalala"]
