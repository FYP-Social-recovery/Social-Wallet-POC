import os
from Crypto.Cipher import AES
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

class SymmetricEncryption:
    def encrypt_vault_512_bit_key(file_content):
        # 512-bit key
        key = os.urandom(64)

        # Salt should be a random value that is unique for each key derivation
        salt = os.urandom(16)

        # Number of iterations should be high enough to make the key derivation slow
        iterations = 100000

        # Derive a 256-bit key using PBKDF2
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256,
            length=32,
            salt=salt,
            iterations=iterations,
            backend=default_backend()
        )

        key = kdf.derive(key)

        # Generate a 16-byte initialization vector (IV)
        iv = os.urandom(16)

        cipher = AES.new(key, AES.MODE_CBC, iv)

        # The string to be encrypted
        plaintext = file_content

        # Padding the plaintext to a multiple of 16 bytes
        padding = 16 - (len(plaintext) % 16)
        plaintext += bytes([padding]) * padding

        # Encrypting the plaintext
        ciphertext = cipher.encrypt(plaintext)
        
        # Encoding the ciphertext to base64
        ciphertextBase = base64.b64encode(ciphertext)
        
        with open("../data/vault/encryptedVault.txt", 'w') as file:
            file.write(ciphertextBase.decode())
        
        return ciphertextBase,key,iv

    def encrypt_vault_256_bit_key(file_content):
        # 256-bit key
        key = os.urandom(32)

        # Generate a 16-byte initialization vector (IV)
        iv = os.urandom(16)

        cipher = AES.new(key, AES.MODE_CBC, iv)

        # The string to be encrypted
        plaintext = file_content

        # Padding the plaintext to a multiple of 16 bytes
        padding = 16 - (len(plaintext) % 16)
        plaintext += bytes([padding]) * padding

        # Encrypting the plaintext
        ciphertext = cipher.encrypt(plaintext)
        
        # Encoding the ciphertext to base64
        ciphertextBase = base64.b64encode(ciphertext)
        
        with open("../data/vault/vault.txt", 'w') as file:
            file.write(ciphertextBase.decode())
        
        return ciphertextBase,key,iv
    
    def decrypt_vault(ciphertextBase,key,iv):
        
        # Decoding the ciphertext from base64
        ciphertext = base64.b64decode(ciphertextBase)

        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Decrypting the ciphertext
        plaintext = cipher.decrypt(ciphertext)

        # Removing the padding
        padding = plaintext[-1]
        plaintext = plaintext[:-padding]
        
        with open("../data/vault/decryptedVault.txt", 'w') as file:
            file.write(plaintext.decode())  
            
    def encrypt_vault_128_bit_key(file_content):
        # 256-bit key
        key = os.urandom(16)

        # # Generate a 16-byte initialization vector (IV)
        # iv = os.urandom(16)

        cipher = AES.new(key, AES.MODE_ECB)

        # The string to be encrypted
        plaintext = file_content

        # Padding the plaintext to a multiple of 16 bytes
        padding = 16 - (len(plaintext) % 16)
        plaintext += bytes([padding]) * padding

        # Encrypting the plaintext
        ciphertext = cipher.encrypt(plaintext)
        
        # Encoding the ciphertext to base64
        ciphertextBase = base64.b64encode(ciphertext)
        
        # with open("../data/vault/vault.txt", 'w') as file:
        #     file.write(ciphertextBase.decode())
        
        return ciphertextBase,key
    
    def decrypt_vault_128(ciphertextBase,key):
        
        # Decoding the ciphertext from base64
        ciphertext = base64.b64decode(ciphertextBase)

        cipher = AES.new(key, AES.MODE_ECB)

        # Decrypting the ciphertext
        plaintext = cipher.decrypt(ciphertext)

        # Removing the padding
        padding = plaintext[-1]
        plaintext = plaintext[:-padding]
        
        with open("../data/vault/decryptedVault.txt", 'w') as file:
            file.write(plaintext.decode())  
            
        return plaintext.decode()

    def concatanate2BytesObject(object_1, object_2):
        # Use a known delimiter
        delimiter = b'|'

        # Concatenate the two keys
        concatenated_object = object_1 + delimiter + object_2
        
        return concatenated_object

    def deConcatanate2UnknownLenthBytesObject(concatenated_object):
        delimiter = b'|'
        
        # Deconcatenate the key
        object_1_end = concatenated_object.index(delimiter)
        object_1 = concatenated_object[:object_1_end]
        object_2 = concatenated_object[object_1_end + len(delimiter):]

        return object_1,object_2

    def convertBytesObjectToInteger(byte_object):
        # Convert binary data to integer
        integer_value = int.from_bytes(byte_object, byteorder='big')
        
        return integer_value

    def convertIntegerToBytesObject(integer_value, bytes_length):
        # Convert integer back to bytes data
        byte_object = integer_value.to_bytes(bytes_length, byteorder='big')
        
        return byte_object 
    
    def convertStringToBytesObject(string):
        # Convert String to Bytes object
        byte_object = string.encode('utf-8')
        
        return byte_object
    
    def convertByteToString(byte_object):
        # Convert Byte to string
        string = byte_object.decode('utf-8')
        
        return string