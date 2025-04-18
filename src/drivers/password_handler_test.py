import pytest

from src.drivers.password_handler import PasswordHandler


@pytest.mark.skip(reason="Test OK!")
def test_encrypt():
    minha_senha = "minha_senha"
    password_handler = PasswordHandler()

    hashed_password = password_handler.encrypt_password(minha_senha)
    password_checked = password_handler.check_password(minha_senha, hashed_password)
    assert password_checked
