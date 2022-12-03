import datetime
import time


class Person:

    def __init__(self, name: str, alter: str, plz: int) -> None:
        self.name = name
        self.alter = alter
        self.plz = plz
        self.jahr = jahr


    def calcAge(self):
        jahr = self.alter.split(".")[2]
        self.jahr = int(time.localtime()[0]) - int(self.jahr)
        return self.jahr



    def __str__(self):
        return f"Name: {self.name}, geboren am {self.alter}, wohnhaft in {self.plz}, und {self.jahr} alt"



p1 = Person("Max", "16.09.1997", 1030)
print(p1)
time = time.localtime()[0]
print(time)
