import json
import os
import base64
import hashlib
from cryptography.fernet import Fernet
from getpass import getpass
from typing import Optional

DATA_FILE = "data/passwords.json"

def generate_key(master_password: str) -> bytes:
    hash_digest = hashlib.sha256(master_password.encode()).digest()
    return base64.urlsafe_b64encode(hash_digest)

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def encrypt_data(fernet: Fernet, plaintext: str) -> str:
    return fernet.encrypt(plaintext.encode()).decode()

def decrypt_data(fernet: Fernet, ciphertext: str) -> str:
    return fernet.decrypt(ciphertext.encode()).decode()

def add_password(site: str, username: str, password: str, fernet: Fernet):
    data = load_data()
    data[site] = {
        "username": encrypt_data(fernet, username),
        "password": encrypt_data(fernet, password)
    }
    save_data(data)

def get_password(site: str, fernet: Fernet) -> Optional[dict]:
    data = load_data()
    if site in data:
        try:
            return {
                "username": decrypt_data(fernet, data[site]["username"]),
                "password": decrypt_data(fernet, data[site]["password"])
            }
        except:
            return None
    return None

def validate_input(text: str) -> bool:
    return bool(text.strip())
