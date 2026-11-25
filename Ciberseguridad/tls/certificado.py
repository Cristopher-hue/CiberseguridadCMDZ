import datetime
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID


def gen_llaves_privada():
  private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
  with open("private.pem", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )
  return private_key


def gen_llave_publica(private_key):
  # Extraemos la clave pública del MISMO par que la clave privada
  public_key = private_key.public_key()
  with open("public.pem", "wb") as f:
    f.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
    )
  return public_key


def gen_certificado(public_key, private_key):
  subject = issuer = x509.Name([
      x509.NameAttribute(NameOID.COUNTRY_NAME, "MX"),
      x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Puebla"),
      x509.NameAttribute(NameOID.LOCALITY_NAME, "Zacapoaxtla"),
      x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Sistemas en Seguridad"),
      x509.NameAttribute(NameOID.COMMON_NAME, "seguridad.com"),
  ])

  cert = (
      x509.CertificateBuilder()
      .subject_name(subject)
      .issuer_name(issuer)
      .public_key(public_key)
      .serial_number(x509.random_serial_number())
      .not_valid_before(datetime.datetime.utcnow())
      .not_valid_after(
          datetime.datetime.utcnow() + datetime.timedelta(days=365)
      )
      .sign(private_key, hashes.SHA256())
  )

  with open("certificado.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))


private_key = gen_llaves_privada()
public_key = gen_llave_publica(private_key)  # Le pasamos la clave privada
gen_certificado(public_key, private_key)