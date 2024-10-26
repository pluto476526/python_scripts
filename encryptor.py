from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import os
import base64
import secrets

# Function to derive a key from the password
def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

# Function to encrypt a file
def encrypt_file(file_name: str, password: str):
    salt = secrets.token_bytes(16)  # Generate a random salt
    key = derive_key(password, salt)
    fernet = Fernet(key)

    with open(file_name, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    # Create a new random filename (shortened to 5 characters)
    new_file_name = f"file_{secrets.token_hex(3)}.encrypted"  # Random hex string of 3 bytes (6 hex chars)
    
    with open(new_file_name, 'wb') as encrypted_file:
        # Prepend salt and original filename length and name for later retrieval
        encrypted_file.write(salt + len(file_name).to_bytes(4, 'big') + file_name.encode() + encrypted)

    print(f"{file_name} has been encrypted and renamed to {new_file_name}")

    # Delete the original file after successful encryption
    os.remove(file_name)
    print(f"The original file {file_name} has been deleted.")

# Function to decrypt a file
def decrypt_file(file_name: str, password: str):
    with open(file_name, 'rb') as enc_file:
        data = enc_file.read()

    salt = data[:16]  # Extract the salt from the beginning of the file
    original_filename_length = int.from_bytes(data[16:20], 'big')  # Get the length of the original filename
    original_filename = data[20:20 + original_filename_length].decode('utf-8')  # Extract the original filename
    encrypted_data = data[20 + original_filename_length:]  # The rest is the encrypted data

    key = derive_key(password, salt)
    fernet = Fernet(key)

    decrypted = fernet.decrypt(encrypted_data)

    # Save decrypted content using the original filename in the current working directory
    with open(original_filename, 'wb') as dec_file:
        dec_file.write(decrypted)

    print(f"{file_name} has been decrypted and saved as {original_filename}")

# Main function to execute the script
if __name__ == "__main__":
    action = input("Do you want to (e)ncrypt or (d)ecrypt files? ").lower()
    
    if action == 'e':
        filenames = input("Enter the filenames to encrypt (comma-separated): ")
        password = input("Enter a password for encryption: ")
        for filename in [f.strip() for f in filenames.split(',')]:
            if os.path.isfile(filename):
                encrypt_file(filename, password)
            else:
                print(f"File {filename} does not exist.")
        
    elif action == 'd':
        filenames = input("Enter the filenames to decrypt (comma-separated): ")
        password = input("Enter your password for decryption: ")
        for filename in [f.strip() for f in filenames.split(',')]:
            if os.path.isfile(filename):
                decrypt_file(filename, password)
            else:
                print(f"File {filename} does not exist.")
        
    else:
        print("Invalid action. Please choose 'e' or 'd'.")