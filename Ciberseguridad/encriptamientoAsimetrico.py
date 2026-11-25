import hashlib
import rsa


def llave_publica():
    with open("public_key1.pem", "rb") as file:
        public_key = rsa.PublicKey.load_pkcs1(file.read())
    return public_key


def llave_privada():
    with open("private_key1.pem", "rb") as file:
        private_key = rsa.PrivateKey.load_pkcs1(file.read())
    return private_key


# obteniendo hash de documento
def hash_documento(documento_path):
    sha = hashlib.sha256()
    with open(documento_path, "rb") as file:
        for blokes in iter(lambda: file.read(2048), b""):
            sha.update(blokes)
    return sha.digest()


def firmar_documento(documento_path, llave_publica):
    hash_doc = hash_documento(documento_path)
    firma = rsa.encrypt(hash_doc, llave_publica)
    with open("firma_documento.bin", "wb") as file:
        file.write(firma)
    print("Documento firmado correctamente.")


def verificar_firma(documento_path, llave_privada):
    hash_doc = hash_documento(documento_path)
    try:
        with open("firma_documento.bin", "rb") as file:
            firmar_documento = file.read()
            hash_firma_verificada = rsa.decrypt(firmar_documento, llave_privada)
            if hash_doc == hash_firma_verificada:
                print("La firma es válida. El documento no ha sido alterado.")
            else:
                print("La firma NO es válida. El documento ha sido alterado.")
    except Exception as e:
        print(f"Error al verificar la firma: {e}")



if __name__ == "__main__":
    pub_key = llave_publica()
    priv_key = llave_privada()

    while True:
        print("\n--- MENÚ DE FIRMA DIGITAL ---")
        print("1. Firmar documento / imagen")
        print("2. Verificar documento / imagen")
        print("3. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            documento_path = input("nombre del archivo (ej. imagen.png o archivo.pdf): ").strip()
            firmar_documento(documento_path, pub_key)

        elif opcion == "2":
            documento_path = input("Ingresa la ruta del archivo a verificar: ").strip()
            verificar_firma(documento_path, priv_key)

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")