"""
<U1 Bsp. 3>
<Rabat-Rechner>
<Maximilian Jonas, 52203295>
"""
### Programm das automatisch den Rabat anhand eines Betrages berechnet
import os

# Funktion zum Löschen des Terminals
def clear():

    # überprüft ob das Betriebsystem Windows ist
    if os.name == "nt":
        os.system("cls") # löscht Konsole

    else:
        os.system("clear") # löscht Konsole



# String detection

while True:

    try: # versucht einen string oder float in "betrag" zu speichern, bei Erfolg wird der Loop unterbrochen

        betrag = eval(str(input("Betrag (€): ").replace(",", ".")))
        break



    except: # kommt es zu einem Type Error wird die Konsole gelöscht und die Eingabe wiederholt

        clear()

        print("Wiederholen sie die Eingabe mit einem Gedbetrag")
        continue


if betrag < 1000: # überprüft ob betrag kleiner als 1000€ ist

    rabat = betrag * 0.95 # errechnet und speichert den Rabat mit Skonto in "rabat"

elif betrag >= 1000 and betrag <= 1999: #Überprüft ob betrag zwischen 1000 und 1999€ liegt

    rabat = betrag * 0.90 # errechnet und speichert den Rabat mit Skonto in "rabat"

elif betrag >= 2000 and betrag <= 4999: #Überprüft ob betrag zwischen 2000 und 4999€ liegt

    rabatOs = betrag * 0.85 # errechnet und speichert den Rabat ohne Skonto in "rabatOs"
    rabat = rabatOs * 0.98 # errechnet und speichert den Rabat mit Skonto in "rabat"

else:

    rabatOs = betrag * 0.80 # errechnet und speichert den Rabat ohne Skonto in "rabatOs"
    rabat = rabatOs * 0.97 # errechnet und speichert den Rabat mit Skonto in "rabat"


# "rabat" wird zu einem String verändert um nur 2 Dezimalstelln und anstatt eines "." einen "," auszugeben

rabatString = str(rabat).replace(".", ",").split(",")
rabat = rabatString[0] + "," + rabatString[1][:2]

# Ausgabe desZahlungsbetrages
print(f"Zahlungsbetrag: {rabat} €")