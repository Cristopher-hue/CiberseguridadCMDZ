import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms,modes
from cryptography.hazmat.primitives import padding

key_aes = os.urandom(32)
padding_aes = padding.ANSIX923(128).padder()
data = "Mensaje a encriptar"
data2 = data.encode("UTF-8")
cipher = Cipher(algorithms.AES(key_aes), modes.CBC(os.urandom(16)))
cifrador = cipher.encryptor()
texto_cifrado = cifrador.update(padding_aes.update(data2) + padding_aes.finalize()) + cifrador.finalize()
print("Mensaje a encriptar: ", data)
print(texto_cifrado)

descifrador = cipher.decryptor()
unpadder = padding.ANSIX923(128).unpadder()
texto_descifrado = unpadder.update(descifrador.update(texto_cifrado) + descifrador.finalize()) + unpadder.finalize()
print("Mensahe descifrado: ", texto_descifrado.decode("UTF=8"))