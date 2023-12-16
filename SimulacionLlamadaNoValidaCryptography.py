from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import jwt
import datetime

# Llave privada del Servidor de Firma (STI-AS)
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Número de teléfono del llamante
caller_number = "6076817387"

# Crear el token JWT
token = jwt.encode(
    {
        "iss": "servidor_firma",
        "iat": datetime.datetime.utcnow(),
        "orig": caller_number,
    },
    private_key,
    algorithm='RS256'
)

print(f"Llamada firmada: {token}")

# Llave pública del Servidor de Verificación (STI-VS)
public_key = private_key.public_key()

# Número de teléfono del llamante
caller_number = "6076817387"

# Token firmado (simulado)
signed_token = "TOKEN_FIRMADO_AQUI"

try:
    # Verificar el token JWT
    decoded_payload = jwt.decode(signed_token, public_key, algorithms=['RS256'])

    if decoded_payload['orig'] == caller_number:
        print("Firma válida, la llamada es auténtica.")
    else:
        print("Número de teléfono falsificado. La llamada no es auténtica.")
except jwt.ExpiredSignatureError:
    print("Firma expirada. La llamada no es auténtica.")
except jwt.InvalidTokenError:
    print("Firma no válida. La llamada no es auténtica.")