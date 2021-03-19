import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

key = bytes(str('12345678901234567890123456789012'), 'ascii')
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
encryptor = cipher.encryptor()
ct = encryptor.update(b'a secret message') + encryptor.finalize()
decryptor = cipher.decryptor()
dct = decryptor.update(ct)
print(f'Mensaje encryptado:',ct)
print(f'Mensaje Des-encryptado:',dct)
