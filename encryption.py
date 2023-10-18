from cryptography.fernet import Fernet

def generate_encryption_key():
    return Fernet.generate_key()

def encrypt_private_key(private_key, encryption_key):
    cipher_suite = Fernet(encryption_key)
    encrypted_private_key = cipher_suite.encrypt(private_key.encode())
    return encrypted_private_key

def decrypt_private_key(encrypted_private_key, encryption_key):
    cipher_suite = Fernet(encryption_key)
    private_key = cipher_suite.decrypt(encrypted_private_key).decode()
    return private_key


