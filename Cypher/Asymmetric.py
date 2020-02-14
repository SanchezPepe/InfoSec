from Crypto import Random
from Crypto.PublicKey import RSA
import base64


def generate_keys():
    # RSA modulus length must be a multiple of 256 and >= 1024
    modulus_length = 256*4  # use larger value in production
    privatekey = RSA.generate(modulus_length, Random.new().read)
    publickey = privatekey.publickey()
    return privatekey, publickey


def encrypt_message(data, publickey):
    encrypted_msg = publickey.encrypt(data, 32)[0]
    # base64 encoded strings are database friendly
    encoded_encrypted_msg = base64.b64encode(encrypted_msg)
    return encoded_encrypted_msg


def decrypt_message(encoded_encrypted_msg, privatekey):
    decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
    decoded_decrypted_msg = privatekey.decrypt(decoded_encrypted_msg)
    return decoded_decrypted_msg


# data = "The quick brown fox jumped over the lazy dog"
archivo = open('RSA.py', 'rb')
data = archivo.read()
archivo.close()

privatekey, publickey = generate_keys()
encrypted_msg = encrypt_message(data, publickey)
decrypted_msg = decrypt_message(encrypted_msg, privatekey)

""" 
print('\n',"%s - (%d)" % (privatekey.exportKey(), len(privatekey.exportKey())), '\n')
print("%s - (%d)" % (publickey.exportKey(), len(publickey.exportKey())), '\n')
"""
print("Mensaje original: \n %s - (%d)" % (data, len(data)), '\n')
print("Cifrado: \n %s - (%d)" % (encrypted_msg, len(encrypted_msg)), '\n')
print("Descifrado: \n %s - (%d)" % (decrypted_msg, len(decrypted_msg)), '\n')
