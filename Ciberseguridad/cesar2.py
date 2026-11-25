def encriptar_cesar(mensaje, llave):
    texto_encriptado=""
    for letra in mensaje:
     codigo_letra= ord(letra)
     nuevo_codigo= codigo_letra + int(llave)
     texto_encriptado += chr(nuevo_codigo)
  
    return texto_encriptado

def desencripatado_cesar(mensaje, llave):
    texto_desipcriptado=""
    for letra in mensaje:
     codigo_letra= ord(letra)
     nuevo_codigo= codigo_letra - int(llave)
     texto_desipcriptado += chr(nuevo_codigo)
  
    return texto_desipcriptado



mensaje = input("Ingrese mensaje a encriptar:")
llave =input("Ingrese la llave de encriptamiento:")
texto_encriptado=""
texto_encriptado=encriptar_cesar(mensaje, llave)
print("mensaje encriptar", texto_encriptado)
print("mensaje desencriptado:", desencripatado_cesar(texto_encriptado, llave))
