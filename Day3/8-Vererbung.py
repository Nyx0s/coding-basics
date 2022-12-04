# class Fh

class Geschäftsführung():

    def __init__(self, name, beliebtheit):

        self.name = name
        self.beliebtheit = beliebtheit

    def __str__(self):
        return f"Name: {self.name} \t Beliebtheit: {self.beliebtheit}"

class Abteilungsleitung():

    def __init__(self, name, beliebtheit, abteilung):

        self.name = name
        self.beliebtheit = beliebtheit
        self.abteilung = abteilung

    def __str__(self):
        return f"Name: {self.name} \t Beliebtheit: {self.beliebtheit} \t Abteilung: {self.abteilung}"


class Mitarbeiter(Abteilungsleitung):

    def __init__(self, name, beliebtheit, abteilung, alter, geschlecht):

        self.alter = alter
        self.geschlecht = geschlecht
        #self.abteilung = abteilung
        super().__init__(name, beliebtheit, abteilung)

    def __str__(self):
        return f"Name: {self.name} \t Beliebtheit: {self.beliebtheit} \t Abteilung: {self.abteilung}\nAlter: {self.alter} \t Geschlecht: {self.geschlecht}"

edi = Mitarbeiter(name="edi", beliebtheit=10, geschlecht="m", alter=25, abteilung="Supp")
eva = Abteilungsleitung(name="eva", beliebtheit=15, abteilung="IT")
print(edi)