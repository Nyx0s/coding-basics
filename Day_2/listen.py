myListe = ["Stp", "Wien", "Klagenfüht", "Salzburg", "Voralberg"]

print(myListe)

# zu liste hinzufügen
myListe.append("Graz")


print(myListe)

#loschen mit pop
myListe.pop() # löscht letztes Element
print(myListe)
myListe.pop(0) # löschen des elements mit index 0 in dem fall stp
print(myListe)

for _ in myListe[:]: # loopt in der liste
    if "al" in _: # prüft ob "al" in einem eintrag innerhalb der liste vokommt
        myListe.remove(_) # löscht einträge die "al" bein´halten
        print(f"{_} wurde Entfert")
        print(myListe)

while True:
    text = input("Text eingeben: ")

    if text == "q":
        print(myListe)
        break

    if text not in myListe:
        myListe.append(text)
        print(f"Text hinzugefügt")
        print(myListe)

    else:
        print(text, "ist bereits in der Liste")





