import socket
import ssl

HOST = '192.168.5.6'
PORT = 4001

contexto = ssl.create_default_context(
    ssl.Purpose.SERVER_AUTH,
    cafile='certificado.crt'
)
contexto.check_hostname = False
contexto.verify_mode = ssl.CERT_NONE

try:
    with socket.create_connection((HOST, PORT)) as conexion:
        with contexto.wrap_socket(conexion, server_hostname='localhost') as cliente:
            print('Conexión realizada con servidor TLS (192.168.5.6)')
            mensaje = 'Practica de conexion segura TLS.....\n'
            cliente.sendall(mensaje.encode('utf-8'))
            print("Mensaje enviado al servidor TLS:", mensaje.strip())

except Exception as e:
    print("Error en la conexión TLS:", e)