import os

from cryptography.hazmat.primitives import hashes

v = '944a1e869969dd8a4b64ca5e6ebc209a'
f1 = open("WinMD5.exe", 'rb')
read = f1.read()
digest = hashes.Hash(hashes.MD5())
digest.update(read)
hash=digest.finalize()
r1 = hash.hex()
print('hash fichero WinMD5.exe:', hash.hex())
if v == r1:
    print('WinMD5.exe es el fichero CORRECTO.')
else:
    print('WinMD5.exe NO es el fichero correcto.')
f1.close()

f2 = open("WinMD5_2.exe", 'rb')
read = f2.read()
digest = hashes.Hash(hashes.MD5())
digest.update(read)
hash=digest.finalize()
r2 = hash.hex()
print('hash fichero WinMD5_2.exe:', hash.hex())
if v == r2:
    print('WinMD5_2.exe es el fichero CORRECTO.')
else:
    print('WinMD5_2.exe NO es el fichero correcto.')
f2.close()