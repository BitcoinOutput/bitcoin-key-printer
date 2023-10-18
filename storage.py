def store_private_key(encrypted_private_key, filename):
    with open(filename, 'wb') as file:
        file.write(encrypted_private_key)

def load_private_key(filename):
    with open(filename, 'rb') as file:
        encrypted_private_key = file.read()
    return encrypted_private_key

