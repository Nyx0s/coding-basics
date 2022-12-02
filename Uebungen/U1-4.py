"""
<U1 Bsp. 4>
<Finde den Unterschied in 4 Strings>
<Maximilian Jonas, 52203295>
"""
### Programm das 2 Stings vergleicht

string1 = input("String1: ").lower() # Speichert einen String und ändert alle Buchstaben zu kleinen Zeichen

string2 = input("String2: ").lower() # Speichert einen String und ändert alle Buchstaben zu kleinen Zeichen

while True: # Überprüft ob der gegebene Integer innerhalb des Index von "string1" und "string" liegt

    if len(string1) == len(string2) and string1 == string2:  # überprüft die länge und Inhalte der ebiden Strings

        integer = int(input(f"Index ( {len(string1[0])}-{len(string1[::1])} ) : "))

        if integer == len(string1): # Wenn "integer" innerhelb des index liegt gib den index von "string1" und "string2" aus und beendet das Programm
            stringIndex = string1[integer - 1]
            print(stringIndex)
            break

        else: # Wenn  "integer" ausßerhalbhalb des index liegt wiederhole die "integer eingabe"
            print(f"Integer auserhalb des Index \n")
            continue




    else:
        print("ungleich")
        break



