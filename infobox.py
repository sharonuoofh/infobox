import os
import sys
import base64
from cryptography.fernet import Fernet
from pathlib import Path
from typing import Union

def generate_key() -> bytes:
    """Generates a key for encryption and decryption."""
    return Fernet.generate_key()

def load_key(key_file: str) -> bytes:
    """Loads a key from a specified file."""
    with open(key_file, 'rb') as file:
        return file.read()

def save_key(key: bytes, key_file: str):
    """Saves a key to a specified file."""
    with open(key_file, 'wb') as file:
        file.write(key)

def encrypt_file(file_path: str, key: bytes):
    """Encrypts a single file."""
    with open(file_path, 'rb') as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)
    print(f"Encrypted {file_path}")

def decrypt_file(file_path: str, key: bytes):
    """Decrypts a single file."""
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    fernet = Fernet(key)
    data = fernet.decrypt(encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(data)
    print(f"Decrypted {file_path}")

def process_folder(folder_path: str, key: bytes, action: str):
    """Encrypts or decrypts all files in a folder."""
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if action == 'encrypt':
                encrypt_file(file_path, key)
            elif action == 'decrypt':
                decrypt_file(file_path, key)

def main(action: str, path: Union[str, Path], key_file: str):
    if action not in ['encrypt', 'decrypt']:
        print("Invalid action. Use 'encrypt' or 'decrypt'.")
        sys.exit(1)

    if not os.path.exists(key_file):
        if action == 'encrypt':
            key = generate_key()
            save_key(key, key_file)
        else:
            print("Key file does not exist. Please provide a valid key file for decryption.")
            sys.exit(1)
    else:
        key = load_key(key_file)

    if os.path.isfile(path):
        if action == 'encrypt':
            encrypt_file(path, key)
        elif action == 'decrypt':
            decrypt_file(path, key)
    elif os.path.isdir(path):
        process_folder(path, key, action)
    else:
        print("Invalid path. Please provide a valid file or folder path.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python infobox.py <encrypt/decrypt> <file/folder path> <key file>")
        sys.exit(1)

    action = sys.argv[1]
    path = sys.argv[2]
    key_file = sys.argv[3]

    main(action, path, key_file)