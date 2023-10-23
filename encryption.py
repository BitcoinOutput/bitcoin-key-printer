import base58
import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.fernet import Fernet

def generate_encryption_key():
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    encryption_key = base58.b58encode(kdf.derive(b'your_secure_password')).decode('utf-8')
    return encryption_key

def encrypt_private_key(private_key, encryption_key):
    private_key_bytes = bytes.fromhex(private_key)
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(base58.b58decode(encryption_key)).decode('utf-8')
    fernet_key = Fernet(key)
    encrypted_private_key = fernet_key.encrypt(private_key_bytes)
    return encrypted_private_key

def decrypt_private_key(encrypted_private_key, encryption_key):
    key = base58.b58encode(kdf.derive(encryption_key.encode())).decode('utf-8')
    fernet_key = Fernet(key)
    private_key_bytes = fernet_key.decrypt(encrypted_private_key)
    private_key_hex = private_key_bytes.hex()
    return private_key_hex

