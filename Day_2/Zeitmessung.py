d = 6400 # 1 Tag in sek
h = 3600 # 1h in sek
m = 60 # 1 min in sek

while True:
    sekunden = int(input("Wie viele Sekunden willst du berechnen? "))

    tage = sekunden // d
    stunden = (sekunden % d) // h
    minuten = (sekunden % d) % h // m
    sek = (sekunden % d) % h % m // 1

    print(tage, stunden, minuten, sek)

    if sekunden == str(sekunden):
        break

