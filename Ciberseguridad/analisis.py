import matplotlib.pyplot as plt
#programa para contar frecuencias de palabras en texto

def leer_archivo(nombre_archivo):
    """
    Lee un archivo de texto y devuelve su contenido como una cadena.
    """
    with open(nombre_archivo, 'r') as archivo:
       contenido = archivo.read()

       contenido_limpio = contenido.lower()  # Convertir a minúsculas
       contenido_limpio = contenido_limpio.replace(" ", "")
       contenido_limpio = contenido_limpio.replace("\n", "")
       contenido_limpio = contenido_limpio.replace("\t", "")  # Eliminar tabulaciones
       contenido_limpio = contenido_limpio.replace("é", "e")  # Eliminar carriage returns
       contenido_limpio = contenido_limpio.replace("á", "a")
       contenido_limpio = contenido_limpio.replace("í", "i")
       contenido_limpio = contenido_limpio.replace("ó", "o")
       contenido_limpio = contenido_limpio.replace("ú", "u")
       contenido_limpio = contenido_limpio.replace("&", "")
       return contenido_limpio


def contar_letras(contenido_limpio):
    diccionario = {}

    if contenido_limpio is None:
        return None

    for letra in contenido_limpio:
        if letra in diccionario:
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1
    return diccionario


def graficar_frecuencias(frecuencias):
    if frecuencias is None:
        return



    caracteres = list(frecuencias.keys())
    valores = list(frecuencias.values())
    plt.bar(caracteres, valores)
    plt.xlabel('Caracteres')
    plt.ylabel('Frecuencia')
    plt.title('Frecuencia de caracteres en el texto')
    plt.show()

def identifica_moda(frecuencias):
   max_frecuencia = max(frecuencias.values())
   moda = [letra for letra, frecuencia in frecuencias.items() if frecuencia == max_frecuencia]
   return moda

if __name__ == "__main__":
    nombre_archivo = input("Ingrese el nombre del archivo de texto: ")
    archivo = leer_archivo(nombre_archivo)
    frecuencias = contar_letras(archivo)
    print("Frecuencias de letras:")
    print(frecuencias)
    graficar_frecuencias(frecuencias)
    moda = identifica_moda(frecuencias)
    print("La letra con mayor frecuencia es:", moda )