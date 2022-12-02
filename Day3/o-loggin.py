"""
Arbeiten mit files (r,w,a)
"""

### schreiben

file = open("file.txt", mode="w", encoding="utf-8")

print("hallo", file=file ) # weiterleitung and Fieldinscriptor

file.close()

with open("file.txt", mode="w", encoding="utf-8") as f:
    print("hallo", file=f)
    f.write("Das ist eine andere möglichkeit text auszulesen")
f.close()

### Lesen

with open("file.txt", mode="r", encoding="utf-8") as fRead:
    #print(fRead.read(), type(fRead.read()))
    print(fRead.readlines())
fRead.close()

