mensaje = input ("Ingrese el mensaje a encriptar:")
llave = input ("Ingrese la llave de encriptamiento:")
texto_encriptado=""
texto_desipcriptado=""
alfabeto="abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

for letra in mensaje:
    if letra in alfabeto:
        posicion=alfabeto.index(letra)
        nueva_posicion = (posicion + int(llave)) % len(alfabeto)
        texto_encriptado += alfabeto[nueva_posicion]
    
print(texto_encriptado)

for letra in texto_encriptado:
    if letra in alfabeto:
        posicion=alfabeto.index(letra)
        nueva_posicion = (posicion - int(llave)) % len(alfabeto)
        texto_desipcriptado += alfabeto[nueva_posicion]

print(texto_desipcriptado)
