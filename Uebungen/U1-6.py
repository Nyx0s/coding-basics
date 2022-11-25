"""
<U1 Bsp. 6>
<Passwort Abfrage>
<Maximilian Jonas, 52203295>
"""

secret = "bis"

counter = 4

while True:

    eingabe = input("Passwort: ")

    if eingabe == secret:
        print("Login erfolgreich")
        break
    elif eingabe == "":
        continue
    elif counter == 0:
        print("Login Gespeert")
        break
    else:
        counter -= 1
        continue