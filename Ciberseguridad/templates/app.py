import os
import rsa
from flask import Flask, jsonify, request, render_template

# Configuración de rutas absolutas automáticas basadas en dónde está guardado este app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# Forzamos a Flask a buscar la carpeta templates al mismo nivel que app.py
app = Flask(__name__, template_folder=TEMPLATES_DIR)

def obtener_llaves():
    pub_path = os.path.join(BASE_DIR, "public_key1.pem")
    priv_path = os.path.join(BASE_DIR, "private_key1.pem")

    # Si las llaves no existen en la carpeta raíz, las crea automáticamente
    if not os.path.exists(pub_path) or not os.path.exists(priv_path):
        pub_key, priv_key = rsa.newkeys(2048)
        with open(pub_path, "wb") as f:
            f.write(pub_key.save_pkcs1())
        with open(priv_path, "wb") as f:
            f.write(priv_key.save_pkcs1())
        print("Claves criptográficas creadas automáticamente en la raíz.")

    # Carga las llaves con rutas absolutas seguras
    with open(pub_path, "rb") as f:
        pub_key = rsa.PublicKey.load_pkcs1(f.read())
    with open(priv_path, "rb") as f:
        priv_key = rsa.PrivateKey.load_pkcs1(f.read())
        
    return pub_key, priv_key

# Carga global de llaves criptográficas
pub_key, priv_key = obtener_llaves()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/firmar", methods=["POST"])
def firmar():
    if "archivo" not in request.files:
        return jsonify({"exito": False, "mensaje": "No se seleccionó ningún archivo."})
    
    file = request.files["archivo"]
    if file.filename == "":
        return jsonify({"exito": False, "mensaje": "Archivo no válido."})

    try:
        contenido = file.read()
        
        # FIRMA DIGITAL CORRECTA: Clave PRIVADA + SHA-256
        firma = rsa.sign(contenido, priv_key, 'SHA-256')
        
        # Guarda el archivo de firma en la raíz del proyecto de forma absoluta
        firma_path = os.path.join(BASE_DIR, "firma_documento.bin")
        with open(firma_path, "wb") as f_out:
            f_out.write(firma)
            
        return jsonify({
            "exito": True, 
            "mensaje": f"El documento '{file.filename}' ha sido firmado correctamente."
        })
    except Exception as e:
        return jsonify({"exito": False, "mensaje": f"Error al firmar: {str(e)}"})

@app.route("/verificar", methods=["POST"])
def verificar():
    if "archivo" not in request.files:
        return jsonify({"exito": False, "mensaje": "No se seleccionó ningún archivo."})

    file = request.files["archivo"]
    if file.filename == "":
        return jsonify({"exito": False, "mensaje": "Archivo no válido."})

    firma_path = os.path.join(BASE_DIR, "firma_documento.bin")
    if not os.path.exists(firma_path):
        return jsonify({"exito": False, "mensaje": "No existe un archivo de firma guardado ('firma_documento.bin'). Firmar primero."})

    try:
        contenido = file.read()

        with open(firma_path, "rb") as f_in:
            firma_guardada = f_in.read()

        # VERIFICACIÓN CORRECTA: Clave PÚBLICA
        rsa.verify(contenido, firma_guardada, pub_key)

        return jsonify({
            "valido": True, 
            "mensaje": "La firma es VÁLIDA. El documento no ha sido alterado."
        })
    except rsa.VerificationError:
        return jsonify({
            "valido": False, 
            "mensaje": "La firma NO es válida. El documento/imagen ha sido alterado."
        })
    except Exception as e:
        return jsonify({
            "valido": False, 
            "mensaje": f"Error al verificar: {str(e)}"
        })

if __name__ == "__main__":
    app.run(debug=True, port=5000)