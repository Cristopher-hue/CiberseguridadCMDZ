import socket
import ssl

HOST = '192.168.5.6'
PORT = 4001

contexto = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
contexto.load_cert_chain('certificado.crt', 'llave.key')

# Cambiado a (HOST, PORT) dentro de una tupla
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.bind((HOST, PORT))  
    servidor.listen()  # Se agregaron los paréntesis ()
    print("Esperando conexión segura del cliente TLS")

    conexion, _ = servidor.accept()

    with conexion:
        # Se corrigió la indentación de las líneas siguientes
        with contexto.wrap_socket(conexion, server_side=True) as cliente:
            print('Conexión segura:', cliente.version())

            with cliente.makefile('rb') as entrada:
                # Corregido salto de línea de '/n' a '\n'
                mensaje = entrada.readline().decode('UTF-8').removesuffix('\n') 

            print('Mensaje del cliente:', mensaje)