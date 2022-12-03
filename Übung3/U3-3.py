import hashlib

def hash_password(passwort):

    hashAlg = hashlib.sha3_256(passwort.encode("utf-8")).hexdigest() # Create HashObject for Hashing SHA-256
    print(f"Hash:\n{hashAlg}")
    return hashAlg

def check_password(oldHash):
    testen = str(input("Gib das zu Überprüfende Passwort erneut ein: "))
    hash_test = hash_password(testen)

    if oldHash == hash_test:
        print("SUCCESS - the entered passwords match")
        return True
    else:
        print("ERROR - the passwords do not match")
        return False


def main():
    firstInput = str(input("Bitte Passwort eingeben: "))
    hash1 = hash_password(firstInput)
    check_password(hash1)

main()