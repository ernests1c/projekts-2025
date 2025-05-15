from cryptography.fernet import Fernet
from secure_password_manager import (
    add_password, get_password, generate_key
)

def test_encryption_decryption(tmp_path, monkeypatch):
    test_file = tmp_path / "passwords.json"
    monkeypatch.setattr("secure_password_manager.DATA_FILE", str(test_file))

    key = generate_key("testmaster")
    fernet = Fernet(key)

    add_password("mytest", "tester", "pass123", fernet)
    result = get_password("mytest", fernet)

    assert result["username"] == "tester"
    assert result["password"] == "pass123"
