"""

<U3 Bsp. 1>
<Der Computer sucht sich zufällig 6 Zahlen von 1-45 aus (gewinnzahlen) danach versucht er so lange 6 Zahlen zufällig zu generiern bis ein Lotto 4er gefunden wurde.>
<Maximilian Jonas, 52203295>

"""
# Importieren der Module
import random
import time


def genNumber(): # Funtion zum erstellen 6 zufälliger Zahlen (im bereich 1-45) und rückgabe als array

    ziehungZahlen = [] # Liste mit Lottozahlen

    count = 6 # Counter für einzelne Zahlen max 6

    while count:

        ziehung = random.randint(1, 45) # Wenn die gegebene Zahl nicht in der Liste "" ist und unter 45 ist füge sie zu Liste "ziehungZahlen" hinzugefügt unde der counter um 1 verringert

        if ziehung not in ziehungZahlen:
            ziehungZahlen.append(ziehung)
            count -= 1


    return ziehungZahlen


def lottoZiehung():

    startZeit = time.time() # speichern der Startzeit des Programmes

    gewinnZahlen = set(genNumber()) # speichern der generierten Lottzeiten (Gewinnzahlen)
    count = 0 # counter für Versusuche
    lottoGew = {"lotto0": 0, "lotto1": 0,"lotto2": 0,"lotto3": 0,"lotto4": 0,"lotto5": 0,"lotto6": 0,} # Dictionary für 0-6 gleiche Zahlen
    zeitVierer = 0 # Variable für die Zeit die benötigt wird um 4 übereinstimmente Zahlen zu finden
    zeitFünf = 0 # Variable für die Zeit die benötigt wird um 5 übereinstimmente Zahlen zu finden
    zeitSechs = 0 # Variable für die Zeit die benötigt wird um 5 übereinstimmente Zahlen zu finden

    print(f"Ihre Gewinnerzahlen: {gewinnZahlen}") #Ausgabe der Fixen Lottozahlen


    while True: # Loop der erst endet wenn zumindest 5 Zahlen übereinstimmen

        guessZahlen = set(genNumber()) # Generieren von 6 zufälligen Zahlen im Bereich 1-45
        correctInt = len(gewinnZahlen.intersection(guessZahlen)) # Vergleich der Gewinnzahl mit der
        count += 1

        # Speichert die einzelnen Lottogewinne
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
            if zeitVierer == False: # zeitViere == 0 also False
                zeitVierer = round((time.time() - startZeit), 2) # speichern der Zeit die benötigt wird 4 übereinstimmende Zahlen zu haben

        if correctInt == 5:
            lottoGew["lotto5"] += 1
            if zeitFünf == False:  # zeitFünf == 0 also False
                zeitFünf = round((time.time() - startZeit), 2)
                break # beenden des Loops nachdem 5 übereinstimmende Zahlen gefunden wurden


        if correctInt == 6:
            lottoGew["lotto6"] += 1
            if zeitSechs == False:
                zeitSechs = round((time.time() - startZeit), 2)
                #break
    # Ausgabe der Veruche und Zeit die benötigt wird um einen Lotto 4,5,6er zu erhalten
    print(f"Versuche: {count}\nZeit 4er: {zeitVierer}s\nZeit 5er: {zeitFünf}s\nZeit 6er: {zeitSechs}s")





lottoZiehung()