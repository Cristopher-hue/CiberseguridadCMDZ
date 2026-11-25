import hashlib

texto = "prueba de hash"
hash_fijo = hashlib.sha1(texto.encode("UTF-8")).hexdigest()
print("Texto original:", texto)
print("Hash SHA1:", hash_fijo)
hash_fijo2 = hashlib.sha256(texto.encode("UTF-8")).hexdigest()
print("Hash sha256", hash_fijo2)

with open("duck2.jpg", "rb") as file: 
    pato = file.read()
    hash_pato = hashlib.sha256(pato).hexdigest()
    file.close()
print("Hash SHA256 de duck2.jpg: ", hash_pato)