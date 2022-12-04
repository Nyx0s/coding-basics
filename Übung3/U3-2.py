"""

<U3 Bsp. 2>
<Generieren eines Passwortes das zwischen 10 u. 16. Zeichen Lang ist und mindestens 2 klein Buchstaben 2 Großbuchstaben2 Zahlen und 2 SOnderzeichen besteh>
<Maximilian Jonas, 52203295>

"""
# Import Module
import random
import  string

# erzeugt Variablen die alle zeiechen unterteilt beinhalten
genStrLowPassword = string.ascii_lowercase # Kleinbuchstaben
genStrHighPassword = string.ascii_uppercase # Großbuchstaben
genDigitPassword = string.digits # Zahlen
genSymbPassword = string.punctuation # Zeichen


# erzeugt eine Variable die alle möglichen Zeichen enthält
all = genSymbPassword + genDigitPassword + genStrHighPassword + genStrLowPassword

# Loop der das Passwort wählt
while True:
    genPassword = [] # liste mit zeichen
    print(genPassword)
    for password in range(random.randint(10, 16)): # wählt zufällig 10-16 zeichen als länge für das Passwort
        genPassword += random.choice(all) # wählt zufällige Zeichen aus All aus

    # beendet den loop erst wenn mindesten 2 Kleinbuchstaben, 2 Großbuchstaben, 2 Zahlen, 2 Zeichen in "genPassword" enthalten sind
    if (sum(char in genSymbPassword for char in genPassword) >= 2 and
            sum(char in genDigitPassword for char in genPassword) >= 2 and sum(char in genStrLowPassword for char in genPassword)>= 2  and sum(char in genStrHighPassword for char in genPassword)>= 2):
        break


random.shuffle(genPassword) # mischen der Liste
mypassword = "" .join(genPassword) # erstellen eines Strings aus "genPasswort"

print(f"Ihr Passwort: {mypassword} mit einer Länge von {len(mypassword)} Zeichen")

