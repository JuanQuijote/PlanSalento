import time
from jose import jwt
import base64

ts = int(time.time())
secret = "secreto1"

def encode_b(dataRow):
    print(dataRow[0])
    token = jwt.encode({"id": dataRow[0], "role": dataRow[11], "time":10000}, secret, algorithm='HS256')
    return token 

def encode_u(dataRow):
    print(dataRow[0])
    token = jwt.encode({"id": dataRow[0], "role": dataRow[9], "time":10000}, secret, algorithm='HS256')
    return token 

def decode_tk(token):

    print("/auth: ",token)

    result = jwt.decode(token, secret, algorithms=['HS256'])
    print("resultado decode: ",result)
    return result
    """
    parts = token.split(".")
    if len(parts) != 3:
        raise Exception("Incorrect id token format")
    payload = parts[1]
    padded = payload + "=" * (4 - len(payload) % 4)
    decoded = base64.b64decode(padded)
    print(decoded)
    """
    #key = token
    #key = token.decode('utf-8')
    #key = decoded.decode('utf-8')
    #print(key)

    
    
    