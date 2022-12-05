"""

<U3 Bsp. 2>
<Generieren eines Passwortes das zwischen 10 u. 16. Zeichen Lang ist und mindestens 2 klein Buchstaben 2 Großbuchstaben2 Zahlen und 2 SOnderzeichen besteh>
<Maximilian Jonas, 52203295>

"""
# Import Module
import hashlib

def hash_password(passwort): # funktion zum Erstellen eines Hashes

    hashAlg = hashlib.sha3_256(passwort.encode("utf-8")).hexdigest() # Create HashObject for Hashing SHA-256
    print(f"Hash:\n{hashAlg}")
    return hashAlg

def check_password(oldHash): # Funtion zum Überprüfen des Hashes
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