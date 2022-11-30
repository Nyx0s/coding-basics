"""

<U2 Bsp. 2>
<String auf Palindrome überprüfen>
<Maximilian Jonas, 52203295>

"""

stringOP = str(input("Wort eingeben: ")).lower() # Nimmt einen String vom user und verwendelt ihn in kleinbuchstaben


print(stringOP == stringOP[::-1]) # ausgabe Boolian ob "stringOP" der selbe is wenn "stringOP" gespiegelt wird