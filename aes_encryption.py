import os
import sys
from Crypto.Cipher import AES

def pad(data):
    padding_length = 16 - len(data) % 16
    padding = bytes([padding_length] * padding_length)
    return data + padding

def encrypt_file(input_file, output_file):
    key = os.urandom(32)
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        with open(input_file, 'rb') as f:
            plaintext = f.read()
        padded_plaintext = pad(plaintext)
        ciphertext = cipher.encrypt(padded_plaintext)
        with open(output_file, 'wb') as f:
            f.write(ciphertext)
        encoded_key = key.hex()
        encoded_iv = iv.hex()
        return encoded_key, encoded_iv
    except Exception as e:
        print(f"An error occurred during encryption: {e}")
        return None, None

if __name__ == "__main__":
    input_file = sys.argv[1]
    encrypted_file = "Encrypted_"+ sys.argv[1]
    

    # Encrypt the file
    key, iv = encrypt_file(input_file, encrypted_file)
    if key and iv:
        print("File encrypted successfully.")
        print("Key:", key)
        print("IV:", iv)
    else:
        print("Encryption failed.")