def meineFunktion(zahl1=5, zahl2=3) -> int:
    """
    Meine Funktion
    """

    return zahl1 - zahl2, print("Funkt")


erg, text = meineFunktion(8, 10)
print(erg, text)
erg, text = meineFunktion(zahl2=10, zahl1=8)
print(erg, text)