mensaje_encriptado = input("Ingrese el mesaje a encriptar:")

alfabeto="abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
cripoanalisis =""
for posicion in range(len(alfabeto)):
    for letra in mensaje_encriptado:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            nueva_posicion=(indice-posicion)% len(alfabeto)
            cripoanalisis += alfabeto[nueva_posicion]

    print (f"Posicion {posicion}: {cripoanalisis} resultado")
    cripoanalisis=""
