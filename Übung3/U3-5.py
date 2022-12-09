"""

<U3 Bsp. 2>
<Unterteilen von gegebenen Personen mithilfe einer Klasse>
<Maximilian Jonas, 52203295>

"""
# Import Module
import time


class Person:

    def __init__(self, name: str, alter: str, plz: int):  # Konstruieren der Variablen für den Namen das Ater
        self.name = name
        self.alter = alter
        self.plz = plz
        self.jahr = self.alter.split(".")[2]
        self.jahr = self.calcAge()


    def calcAge(self):
        datum = int(time.localtime()[0])
        self.jahr = datum - int(self.jahr)
        return self.jahr

    def __str__(self):
        return f"{self.name}, geboren am {self.alter}, wohnhaft in {self.plz} ist {self.jahr} Jahre alt."


p1 = Person('Alfred Maurer', '08.06.2001', 3100)
p2 = Person('Lisa Winkler', '22.05.1992', 1100)
p3 = Person('Ernst Hindler', '01.10.1919', 1120)

#p1.calcAge()
print(p1)
# p2.calcAge()
# print(p2)
# p3.calcAge()
# print(p3)
