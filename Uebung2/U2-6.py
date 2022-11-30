"""

<U2 Bsp. 6>
<Satz in Buchstaben unterteilen und diese Zählen>
<Maximilian Jonas, 52203295>

"""
sentence = 'Jim quickly realized that the beautiful gowns are expensive'
letterDic = {} # Erzeugen eines Dictionarys

for letter in sentence:
    if letter not in letterDic: # Hinzufügen eines Buchstabens als Key wenn er nicht in "letterDic"
        letterDic[letter] = sentence.count(letter) # Zählen und speichern des Buchstabens

letterDic.pop(" ") # Löschen des Eintrages " "
for x,y in letterDic.items(): # AUsgeben von Key und Value des Dic "letterDic"
    print(f"Buchstabe {x}: {y}")
