"""

<U2 Bsp. 2>
<String auf Palindrome überprüfen>
<Maximilian Jonas, 52203295>

"""

stringOP = str(input("Wort eingeben: ")).lower()

#stringRev = stringOP.__reversed__()
print(stringOP == stringOP[::-1])
