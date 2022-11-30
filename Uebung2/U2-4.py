"""

<U2 Bsp. 4>
<Dictionary manipulieren>
<Maximilian Jonas, 52203295>

"""

pets = {'cat': 4, 'dog': 15, 'bird': 5, 'velociraptor': 150} # Gegebenes Dict

pets['mouse'] = 1 # Hinzufügen des keys "mouse" mit value 1
pets['dog'] = 20 # Ändern des values von "dag" auf 2ß
pets.pop('bird') # Löschen des keys "bird" sammt Value

for key, value in pets.items(): # AUsgeben der Keys und Values in Dic "pets"
    print(f" {key}: {value}")