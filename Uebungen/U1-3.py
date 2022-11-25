"""
<U1 Bsp. 1>
<Rabat-Rechner>
<Maximilian Jonas, 52203295>
"""
### Programm das automatisch den Rabat anhand eines Betrages berechnet

betrag = eval(input("Betrag (€): "))

if betrag < 1000:

    rabat = betrag * 0.95

elif betrag >= 1000 and betrag <= 1999:

    rabat = betrag * 0.90

elif betrag >= 2000 and betrag <= 4999:

    rabatOs = betrag * 0.85
    rabat = rabatOs * 0.98

else:

    rabatOs = betrag * 0.80
    rabat = rabatOs * 0.97

print(f"Zahlungsbetrag: {rabat}€")