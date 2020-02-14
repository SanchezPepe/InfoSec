import base64

""" Cifrado DES """
from Crypto.Cipher import DES

with open("README.md", "rb") as binary_file:
    data = binary_file.read()

def des_Cypher(key, data):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(data)
    encrypted_text = des.encrypt(padded_text)
    return encrypted_text

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

key = 'hello123'
text = 'Mensaje a cifrar'

print("Mensaje a cifrar: ", text)
print("Cifrado: ", base64.encodestring(des_Cypher(key, text)))

