from key_generation import generate_keypair
from encryption import encrypt_private_key, decrypt_private_key
from encryption import generate_encryption_key
from code_generation import generate_qrcode
from storage import store_private_key, load_private_key

def print_menu():
    print("1. Generate Key Pair")
    print("2. Encrypt and Store Private Key")
    print("3. Generate QR Code")
    print("4. Exit")

encryption_key = generate_encryption_key()  # Generate the encryption key once

def main_menu():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            private_key, public_key_compressed, bitcoin_address = generate_keypair()
            print(f"Private Key: {private_key}")
            print(f"Compressed Public Key: {public_key_compressed}")
            print(f"Bitcoin Address: {bitcoin_address}")

        elif choice == "2":
            # Generate encryption key
            encryption_key = generate_encryption_key()

            private_key = input("Enter your private key: ")
            encrypted_private_key = encrypt_private_key(private_key, encryption_key)
            print(f"Encrypted Private Key: {encrypted_private_key.decode()}")

        elif choice == "3":
            public_key = input("Enter your public key: ")
            generate_qrcode(public_key)
            print("QR code generated and saved as qrcode.png.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")
     
if __name__ == "__main__":
    main_menu()
