import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# CIFRADO CON AES Y CBC
key = bytes(str('12345678901234567890123456789012'), 'ascii')
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
encryptor = cipher.encryptor()
ct = encryptor.update(b"a secret message") + encryptor.finalize()
# DESCIFRADO
decryptor = cipher.decryptor()
dct = decryptor.update(ct) + decryptor.finalize()

# MOSTRAMOS MENSAJE POR PANTALLA
print(f'Mensaje encryptado:',ct)
print(f'Mensaje encryptado hexadecimal:',ct.hex())
print(f'Mensaje Des-encryptado:',dct.decode('utf-8'))
