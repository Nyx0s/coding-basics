"""

<U2 Bsp. 2>
<2 Listen auf Dublikate überprüfen>
<Maximilian Jonas, 52203295>

"""

a = [1, 1, 'hello', 'hello', 2, 5, 8, 13, 22, 2, 'world']
b = [55, 5, 1, 2, 2, 5]

# Combiniert "a" und "b" als set
setComb = set(a).union(set(b))
print(setComb)

# Gibt die Unterschiede von "a" und "b" an
setDiff = set(a).difference(set(b))
print(setDiff)

# sortieren von Liste "b"
setSort = sorted(set(b))
print(setSort)


