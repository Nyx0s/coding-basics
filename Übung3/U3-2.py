import random
import  string

genStrLowPassword = string.ascii_lowercase
genStrHighPassword = string.ascii_uppercase
genDigitPassword = string.digits
genSymbPassword = string.punctuation

all = genSymbPassword + genDigitPassword + genStrHighPassword + genStrLowPassword

while True:
    genPassword = []
    for password in range(random.randint(10, 16)):
        genPassword += random.choice(all)

    if (sum(char in genSymbPassword for char in genPassword) >= 2 and
            sum(char in genDigitPassword for char in genPassword) >= 2 and sum(char in genStrLowPassword for char in genPassword)>= 2  and sum(char in genStrHighPassword for char in genPassword)>= 2):
        break


random.shuffle(genPassword)
mypassword ="" .join(genPassword)

print(f"Ihr Passwort: {mypassword} mit einer Länge von {len(mypassword)} ZeicheN")

