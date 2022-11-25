"""
<U1 Bsp. 1>
<Finde den Unterschied in 2 Strings>
<Maximilian Jonas, 52203295>
"""
### Programm das 2 Stings vergleicht

string1 = input("String1: ").lower()

string2 = input("String2: ").lower()

integer = eval(input("Index: "))

print("")

if len(string1) == len(string2) and string1 == string2:
    stringIndex = string1[integer].upper()
    print(stringIndex)
else:
    print("ungleich")