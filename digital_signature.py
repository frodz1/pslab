from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.exceptions import InvalidSignature
import sys


#Generowanie kluczy publicznego i prywatnego
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

#Zmienne pomocnicze

# Zapisanie kluczy do plików
with open("private_key.pem", "wb") as file:
    file.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open("public_key.pem", "wb") as file:
    file.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

#Wczytanie pliku do podpisania
file_path = sys.argv[1]
with open(file_path, "rb") as file:
    data = file.read()

#Podpisanie pliku kluczem prywatnym
signature = private_key.sign(
    data,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

#Zapisanie podpisu
with open("signature.bin", "wb") as file:
    file.write(signature)

print("Plik został podpisany cyfrowo.")
