"""
<U1 Bsp. 1>
<Summierer>
<Maximilian Jonas, 52203295>
"""
### Programm das alle Zahlen von 1 - 50 addiert

summe = 0 # speichert den Wert innerhalb des Loops

for zahl in range(1, 51): # Erzeugt Loop der alle Zalen von 1-50 durchgeht
    summe = summe + zahl # addiere die Aktuelle zahl des Loops zu der Summe

print(f"Ergebis = {summe}") # Ausgabe der Variable Summe