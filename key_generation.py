import ecdsa
import base58
import hashlib
import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def generate_keypair():
    # Generate a private key
    private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    public_key = private_key.get_verifying_key()

    # Get the hexadecimal representation of the private key
    private_key_hex = private_key.to_string().hex()

    # Get the compressed public key (66 characters)
    public_key_compressed = "02" + public_key.to_string().hex() if public_key.pubkey.point.y() % 2 == 0 else "03" + public_key.to_string().hex()

    # Generate the Bitcoin address
    bitcoin_address = generate_bitcoin_address(public_key_compressed)

    return private_key_hex, public_key_compressed, bitcoin_address

def generate_bitcoin_address(public_key_compressed):
    # Perform the RIPEMD160 hash
    ripemd160_hash = hashlib.new('ripemd160')
    ripemd160_hash.update(hashlib.sha256(bytes.fromhex(public_key_compressed)).digest())
    ripemd160_hash_bytes = ripemd160_hash.digest()

    # Add the version byte (0x00 for MainNet)
    versioned_ripemd160_hash = b'\x00' + ripemd160_hash_bytes

    # Calculate the checksum (first 4 bytes of double SHA-256 hash)
    checksum = hashlib.sha256(hashlib.sha256(versioned_ripemd160_hash).digest()).digest()[:4]

    # Append the checksum to the versioned RIPEMD-160 hash
    extended_ripemd160 = versioned_ripemd160_hash + checksum

    # Encode the extended RIPEMD-160 hash with checksum in Base58Check format
    bitcoin_address = base58.b58encode(extended_ripemd160).decode('utf-8')

    return bitcoin_address

