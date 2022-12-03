import cmath
class Kreis:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return cmath.pi * self.radius ** 2

    def circumference(self):
        return 2 * cmath.pi * self.radius


class Rechteck:
    def __init__(self, length, height):
        self.length = length
        self.hight = height

    def area(self):
        return self.length * self.hight

    def circumference(self):
        return 2 * self.length + 2 * self.hight


class Quadrat:
    def __init__(self, size):
        self.size = size

    def area(self):
        return self.size ** 2

    def circumference(self):
        return self.size * 4

obj = [
    Kreis(7.1),
    Kreis(4.8),
    Rechteck(3.1, 7.4),
    Quadrat(6)
]

for i in obj:
    print(f'{i.__class__.__name__}:   \tFläche: {i.area():.2f}, Umfang: {i.circumference():.2f}')
