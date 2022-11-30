"""

<U2 Bsp. 1>
<Tuple Manipulation>
<Maximilian Jonas, 52203295>

"""

t = ('P', 'R', 'O', 'G', '1', '_', 'V', 'O') # Tuplen-Liste gefüllt mit Strings

# Aufgabe 1.1 ausgabe des 3. Elements

print(t[2]) # ausgabe des 3 Elements


# Aufgabe 1.2 ausgabe des zweitletzte Element ausgeben

print(t[-2])


# Aufgab 1.3 tulpe um sich selbst erweitern und ausgeben

tDouble = t * 2 # Verdoppeln des inhaltes der Tuple und speichern in tDouble

print(tDouble) # Ausgabe der Variable t


# Aufgab 1.4 Zählen wie oft der String "O" vorkommt

tCount = t.count("O") # Speichern der häufigkeit von "O" in t
tDoubleCount = tDouble.count("O") # Speichern der häufigkeit von "O" in tDouble

print(f"Innerhalb der gegebenen Tuple {tCount}")
print(f"innerhalb der verdoppelte Tuple {tDoubleCount}")

