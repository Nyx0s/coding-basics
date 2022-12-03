import cmath

class Kreis: # definieren der Klasse Kreis

    def __init__(self, radius): # Konstruieren der Variablen
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


obj = [
    Kreis(7.1),
    Kreis(4.8),
    Rechteck(3.1, 7.4),
    Quadrat(6)
]

for i in obj:
    print(f'{i.__class__.__name__}:   \tFläche: {i.fläche():.2f}, Umfang: {i.umfang():.2f}')
