import hashlib

def hash_password(passwort):

    hashAlg = hashlib.sha3_256() # Create HashObject for Hashing SHA-256
    passwort = passwort.encode("utf-8")

    sha256 = hashAlg.update(passwort,)

    print(sha256    passwort = passwort.encode("utf-8"))

print(hash_password("Hash"))