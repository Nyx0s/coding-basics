import random
"""
Klassen Autos erstellen
Nomaerlweiße werden build-in funktionen innerhalb der klassen verwendet
__init__ [wird benötigt] Konstruktor, d.h parameter werden von Außen an die klasse übergeben
__repr__ [optional] das gleiche wie __str__ für schöne darstellung von Objekten in einer Liste
__del__ [optional] Dekonstruktor - wird aufgerufen wenn eine Classe gelöscht
"""



class Auto():

    # Konstruktor
    def __init__(self, hersteller, typ, farbe, jahr, maxSpeed):

        self.hersteller = hersteller
        self.typ = typ
        self.farbe = farbe
        self.jahr = jahr
        self.maxSpeed = round(random.randint(80,250), 2)
        self.speed = random.randint(60, self.maxSpeed)


    def getTyp(self):
        return self.typ

    def beschleunigung(self):
        print("Beschleunigung")
        self.speed += random.randint(30,60)

        if self.speed > self.maxSpeed:
            print("Vollgas")
            self.speed = self.maxSpeed

        return self.speed



    def bremsen(self):
        print("Bremsen")
        self.speed -= random.randint(10,100)

        if self.speed <= 0:
            print(Vollbremsung)
        return self.speed

    def __str__(self):
        return f"Hersteller: {self.hersteller}\t Typ: {self.typ}\tFabe: {self.farbe}\tJahr:{self.jahr}\t MaxSpeed:{self.maxSpeed}"

    def __repr__(self):
        return f"Hersteller: {self.hersteller}\t Typ: {self.typ}\tFabe: {self.farbe}\tJahr:{self.jahr}\t MaxSpeed:{self.maxSpeed}"


bmw = Auto("BMW", "M4", "silber", 1997, 210)
print(bmw)
print(bmw.getTyp())
print(bmw.beschleunigung())
print(bmw.bremsen())

print("#" * 50)
herstellerListe = ["Audi", "BMW", "Fearia"]
typListe = ["SUV", "Coupe", "Limo", "Van"]
farbListe = ["blau", "rot", "schwarz"]



autoListe = []
for _ in range(int(input("Wieveile Auto-Objekte sollen erstellt werden"))):
    autoListe.append(Auto(hersteller=random.choice(herstellerListe), typ=random.choice(typListe), farbe=random.choice(farbListe), jahr=random.randint(2000, 20022), maxSpeed=random.randint(100,300)))


for _ in autoListe:
    print(_)