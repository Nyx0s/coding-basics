"""

<U3 Bsp. 2>
<Berechnen des Flächeninhalt und Umfang eines Kreises, Rechtecks und Quadrats>
<Maximilian Jonas, 52203295>

"""
# Import Module
import cmath

class Kreis: # definieren der Klasse Kreis

    def __init__(self, radius): # Konstruieren der Klasse
        self.radius = radius

    def fläche(self):
        return cmath.pi * self.radius ** 2
    def umfang(self):
        return cmath.pi * 2 * self.radius


class Rechteck:

    def __init__(self, länge, breite):
        self.länge = länge
        self.breite = breite

    def fläche(self):
        return self.länge * self.breite
    def umfang(self):
        return (self.länge + self.breite) * 2

class Quadrat:

    def __init__(self, länge):
        self.länge = länge

    def fläche(self):
        return self.länge ** 2
    def umfang(self):
        return (self.länge + self.länge) * 2


objekte = [
    Kreis(7.1),
    Kreis(4.8),
    Rechteck(3.1, 7.4),
    Quadrat(6)
]

for objekt in objekte:
    print(f'{objekt.__class__.__name__}:   \tFläche: {objekt.fläche():.2f}, Umfang: {objekt.umfang():.2f}')
