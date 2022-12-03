

class Employee():
    def __int__(self, id, name, salary=1000):
        self.id = id
        self.name = name
        self.salary = salary
       # id = 999 # ist eine Funktionsvariable gilt nur innerhalb funktion

    def __str__(self):
        return f"ID: {self.id}\tName: {self.name}\tGehalt: {self.salary}"

max = Employee(name="Max", id=1000)
eva = Employee(name="Eva", salary=3000)
print(Employee.__str__())