from cryptography.hazmat.primitives.asymmetric import rsa 
from cryptography.hazmat.primitives import serialization

def llave_publica():
    llave = rsa.generate_private_key(public_exponent=65537,key_size=1024)
    with open("public_key.pem","w") as f:
        f.write(llave.public_key().public_bytes
                (encoding=serialization.Encoding.PEM
                 ,format=serialization.PublicFormat.SubjectPublicKeyInfo).decode("UTF-8"))

def llave_privada():
    llave = rsa.generate_private_key(public_exponent=65537,key_size=1024)
    with open("private_key.pem", "w") as f:
        f.write(llave.private_bytes
        (encoding=serialization.Encoding.PEM
        ,format=serialization.PrivateFormat.PKCS8
        ,encryption_algorithm=serialization.NoEncryption()).decode("UTF-8"))

if __name__ == "__main__":
    llave_publica()
    llave_privada()

