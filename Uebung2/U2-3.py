"""

<U2 Bsp. 3>
<2 Listen auf Dublikate überprüfen>
<Maximilian Jonas, 52203295>

"""

a = [1, 1, 'hello', 'hello', 2, 5, 8, 13, 22, 2, 'world'] # Liste "a"
b = [55, 5, 1, 2, 2, 5] # "liste "b"

# Combiniert "a" und "b" als set
setComb = set(a).union(set(b))
print(setComb)

# Gibt die Unterschiede von "a" und "b" an
setDiff = set(a).difference(set(b))
print(setDiff)

# sortieren von Liste "b"
setSort = sorted(set(b))
print(setSort)


