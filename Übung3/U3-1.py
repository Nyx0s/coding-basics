"""

<U3 Bsp. 1>
<Der Computer sucht sich zufällig 6 Zahlen von 1-45 aus (gewinnzahlen) danach versucht er so lange 6 Zahlen zufällig zu generiern bis ein Lotto 4er gefunden wurde.>
<Maximilian Jonas, 52203295>

"""
# Importieren der Module
import random
import time


def genNumber(): # Funtion zum erstellen 6 zufälliger Zahlen (im bereich 1-45) und rückgabe als array

    ziehungZahlen = [] # Liste mit Lottozahlen des Computers für eine Ziehung

    count = 6 # Counter für einzelne Zahlen max 6

    while count:

        ziehung = random.randint(1, 45) # Wenn die gegebene Zahl nicht in der Liste "" ist und unter 45 ist füge sie zu Liste "ziehungZahlen" hinzugefügt unde der counter um 1 verringert

        if ziehung not in ziehungZahlen:
            ziehungZahlen.append(ziehung)
            count -= 1


    return ziehungZahlen


def lottoZiehung():

    startZeit = time.time() #

    gewinnZahlen = set(genNumber())
    count = 0
    lottoGew = {"lotto0": 0, "lotto1": 0,"lotto2": 0,"lotto3": 0,"lotto4": 0,"lotto5": 0,"lotto6": 0,}
    zeitVierer = 0
    zeitFünf = 0
    zeitSechs = 0
    # Mögliche Lotto Combinationen 0-
    print(f"Ihre Gewinnerzahlen: {gewinnZahlen}")


    while True:
        guessZahlen = set(genNumber())
        correctInt = len(gewinnZahlen.intersection(guessZahlen))
        count += 1

        # Speiert die einzelnen Lottoo gewinne
        if correctInt == 0:
            lottoGew["lotto0"] += 1
        if correctInt == 1:
            lottoGew["lotto1"] += 1
        if correctInt == 2:
            lottoGew["lotto2"] += 1
        if correctInt == 3:
            lottoGew["lotto3"] += 1
        if correctInt == 4:
            lottoGew["lotto4"] += 1
            if zeitVierer == False:
                zeitVierer = round((time.time() - startZeit), 2)

        if correctInt == 5:
            lottoGew["lotto5"] += 1
            if zeitFünf == False:
                zeitFünf = round((time.time() - startZeit), 2)
                break


        if correctInt == 6:
            lottoGew["lotto6"] += 1
            if zeitSechs == False:
                zeitSechs = round((time.time() - startZeit), 2)


    print(f"Versuche: {count}\nZeit 4er: {zeitVierer}s\nZeit 5er: {zeitFünf}s\nZeit 6er: {zeitSechs}s")





lottoZiehung()