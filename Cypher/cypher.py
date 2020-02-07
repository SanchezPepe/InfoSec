from Crypto.Cipher import DES
import base64

def desCypher(key, toCypher):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(toCypher)
    print(len(padded_text))
    encrypted_text = des.encrypt(padded_text)
    return encrypted_text

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

key = 'hello123'
text = 'a'

print(base64.encodestring(desCypher(key, text)))

with open("README.md", "rb") as binary_file:
    data = binary_file.read()
    print(data)

