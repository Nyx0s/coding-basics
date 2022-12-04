class Personen():

    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def __str__(self):
        return f"Name: {self.name}, Alter: {self.alter}"

class LehrerIn(Personen):

    def __init__(self, name, alter, schule, klassen):
        self.schule = schule
        self.klassen = klassen
        super().__init__(name, alter)

    def __str__(self):
        return f"Name: {self.name}, Alter: {self.alter}, Schule: {self.schule}, {self.klassen}"

class SportlerIn(Personen):

    def __init__(self, name, alter, sportart, rang):
        self.sportart = sportart
        self.rang = rang
        super().__init__(name, alter)

    def __str__(self):
        return f"Name: {self.name}, Alter: {self.alter}, Sportart: {self.sportart}, Rang: {self.rang}"


class SkifahrerIn(SportlerIn):

    def __init__(self, name, alter, sportart, rang, siege):
        self.siege = siege
        super().__init__(name, alter, sportart, rang)

    def __str__(self):
        return f"Name: {self.name}, Alter: {self.alter}, Sportart: {self.sportart}, Rang: {self.rang} , Siege: {self.siege}"


def main():
 tina = SkifahrerIn('Tina', 18, 'skifahren', 2, 15)
 print(tina)
 print(type(tina))
 max = SportlerIn('Max', 20, 'Tennis', 200)
 print(max)
 print(type(max))
 moritz = LehrerIn('Moritz', 45, 'Real Gymnasium', 5)
 print(moritz)
 print(type(moritz))

main()
