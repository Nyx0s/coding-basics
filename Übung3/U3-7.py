"""

<U3 Bsp. 2>
<Erstellen der Eltern-Klasse Person und 2-Subklassen LehrerIn und SportlerIn. Die SportlerIn klasse bekommt eine Weitere Subklasse Skifahgrer>
Spezialisierung haben.>
<Maximilian Jonas, 52203295>

"""

# Import Module

import time
class IDCard():

    def __init__(self, idn: int, name: str, geburtstag: str, guthaben: float):
        self.idn = idn # identifikations Nummer
        self.name = name
        self.geburtstag = geburtstag
        self.guthaben = guthaben
        self.alter = int(time.localtime()[0]) - int(self.geburtstag.split(".")[2])

    def chargeCredit(self, betrag: int):

        if not (5 <= betrag <= 200):
            raise ValueError(f'Ungültiger Betrag: {betrag}€')
        elif (self.guthaben + betrag) >= 200:
            raise ValueError(f"Das Guthaben darf 200€ nicht überschreiten")
        else:
            self.guthaben += betrag
            print(f'Guthaben für {self.name} wurde aufgeladen - aktueller Stand: {self.guthaben:.2f}')

    def bookService(self, services, extraServices=0):

        match services:
            case 0:
                if self.alter <= 18:
                    raise ValueError(f"Alter für die erwachsenen Karte überschritten")
                self.guthaben -= 25
            case 1:
                self.guthaben -= 18
            case 2:
                self.guthaben -= 12

        match extraServices:
            case 0:
                pass
            case 1:
                self.guthaben -= 5
            case 2:
                self.guthaben -= 10

    def __str__(self):
        return f"Kundennummer: {self.idn}\nName: {self.name}\nGeburtstag: {self.geburtstag}\nAlter: {self.alter}\nGuthaben: {self.guthaben}"


max = IDCard(1, "Max Jonas", "19.06.1997", 10.0)
print(max)
max.chargeCredit(91)
max.bookService(1, 1)
print(max)
