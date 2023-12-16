import json
import time
import hashlib

# Define a class for the Passport Header
class StirShakenHeader:
    def __init__(self, alg, ppt, typ, x5u):
        self.alg = alg
        self.ppt = ppt
        self.typ = typ
        self.x5u = x5u

# Define a class for the Passport Payload
class StirShakenPayload:
    def __init__(self, attest, dest, iat, orig, origid):
        self.attest = attest
        self.dest = dest
        self.iat = iat
        self.orig = orig
        self.origid = origid

# Define a class for the Passport, containing the Header, Payload, and Signature
class StirShakenPassport:
    def __init__(self, header, payload, signature):
        self.header = header
        self.payload = payload
        self.signature = signature

# Function to encode Passport to JSON format
def encode_passport(passport):
    passport_dict = {
        "header": {
            "alg": passport.header.alg,
            "ppt": passport.header.ppt,
            "typ": passport.header.typ,
            "x5u": passport.header.x5u
        },
        "payload": {
            "attest": passport.payload.attest,
            "dest": passport.payload.dest,
            "iat": passport.payload.iat,
            "orig": passport.payload.orig,
            "origid": passport.payload.origid
        },
        "signature": passport.signature
    }
    return json.dumps(passport_dict, indent=2)

# Function to decode Passport from JSON format
def decode_passport(encoded_passport):
    passport_dict = json.loads(encoded_passport)
    header = StirShakenHeader(**passport_dict["header"])
    payload = StirShakenPayload(**passport_dict["payload"])
    signature = passport_dict["signature"]
    return StirShakenPassport(header, payload, signature)

# Function to simulate signing the Passport (generating a simple signature)
def sign_passport(passport):
    data_to_sign = passport.header.alg + passport.payload.attest
    passport.signature = hashlib.sha256(data_to_sign.encode()).hexdigest()

# Function to simulate verifying the Passport signature
def verify_signature(passport):
    data_to_verify = passport.header.alg + passport.payload.attest
    calculated_signature = hashlib.sha256(data_to_verify.encode()).hexdigest()
    return passport.signature == calculated_signature



# Create and initialize StirShakenPassport object with a Header and Payload
header = StirShakenHeader("ES256", "shaken", "passport", "https://shaken.signalwire.cloud/sp.pem")
payload = StirShakenPayload("B", {"tn": ["01256700800"]}, int(time.time()), {"tn": "01256500600"}, "e32f4189-cb86-460f-bb92-bd3acb89f29c")
passport = StirShakenPassport(header, payload, None)

# Encode the Passport to JSON format and print it
encoded_passport = encode_passport(passport)
print("\n1. Passport encoded:")
print(encoded_passport)

# Verify the Passport signature (simulate the verification process)
if verify_signature(passport):
    print("Passport signature is valid.")
else:
    print("Passport signature is invalid.")

    
# Decode the Passport from JSON format and print the decoded Header and Payload
decoded_passport = decode_passport(encoded_passport)
print("\n2. Passport decoded:")
print(f"Header: {decoded_passport.header.__dict__}")
print(f"Payload: {decoded_passport.payload.__dict__}")

# Sign the Passport (simulate the signing process)
sign_passport(passport)
print("\n3. Passport signed.")

# Verify the Passport signature (simulate the verification process)
if verify_signature(passport):
    print("Passport signature is valid.")
else:
    print("Passport signature is invalid.")


