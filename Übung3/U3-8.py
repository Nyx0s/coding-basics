from collections import Counter


liste = [] # Liste für alle inhalte in Einkaufliste (auch doppelte)

try: # Error Handling falls das File nicht existiert
    with open("einkaufsliste.txt", "r", encoding="utf-8") as einkaufsliste: # öffnen von "einkaufsliste" im READ modus
        for _ in einkaufsliste.readlines(): # auslesen aller Zeilen
            item = _.split("\n") # Entfernen von \n in der Liste
            liste.append(item[0]) # Items werden zur Liste hinzugefügt

    einkaufsliste.close()

except FileNotFoundError as e:
    print(f"Die Datei \"einkaufsliste.txt\" existiert nicht - {e}")

counter = Counter(liste) # Erstellen eines Dictionary mit Items als Key und wie oft es vorkommt alls Value

for x,y in counter.items(): # Ausgabe geortneter Liste
    print(f"{y}x -> {x}")

with open("sorted_list", "w", encoding="utf-8") as newList: # Öffnen eines neuen Dokuments im WRITE MODUS
    for x,y in counter.items():
        newList.write(f"{y}x -> {x}\n") # Hinzu fügen der sortierten Einkaufsliste zu dem Dokument
newList.close()
