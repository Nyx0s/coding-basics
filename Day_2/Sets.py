fav0 = {1, 10, 77, -2}
favF = {1, 7, 3, 12, 77}

o = set(fav0)
f = set(favF)

#gleichheiten finden
print("gleiche finden:", o.intersection(f))

# beide sets ohne dublikate zusammenführen
print("Zusammenführen ohne Dublikate:", o.union(f))

fav0_sorted = sorted(o)
favF_sorted = sorted(f)

for _ in fav0_sorted:
    print(_)