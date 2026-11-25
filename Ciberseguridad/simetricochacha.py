import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms,modes
from cryptography.hazmat.primitives import padding

key_chaca = os.urandom(32)
nonce_chaca = os.urandom(16)
data ="Mensaje a encriptar"
data2 = data.encode("utf-8")
chiper_chaca = Cipher(algorithms.ChaCha20(key_chaca,nonce_chaca),None)
encriptador_chacha= chiper_chaca.encryptor()
cifrado_chacha = encriptador_chacha.update(data2) + encriptador_chacha.finalize()
dencriptador_chacha = chiper_chaca.decryptor()
descifrado_chacha = dencriptador_chacha.update(cifrado_chacha) + dencriptador_chacha.finalize()

print("Llave")
print(key_chaca) 
print("Cifrado")
print(cifrado_chacha)
print("Descifrado")
print(descifrado_chacha.decode("UTF-8"))