
"""

<U2 Bsp. 8 und 9>
<Lottozahlen Rechner>
<Maximilian Jonas, 52203295>

"""
import random # Import Random Module

#  Funktion für Spieler-Zahlen
def userZahlen():


    ziehungUser = [] # Liste für Userzahlen

    count = 6 # Counter für einzelne Zahlen max 6
    while count:


        try:

            ziehung = int(input("User input: ")) # Speicher inpuut in "ziehung"

            if ziehung not in ziehungUser: # Wenn die gegebene Zahl nicht in der Liste "ziehungUser" ist und unter 45 ist füge sie zu Liste "ziehungUser" hinzugefügt unde der counter um 1 verringert
                if ziehung <= 45 and ziehung >= 1:
                    ziehungUser.append(int(ziehung))
                    count -= 1
                else:
                    print("Zahl ist kleiner als 1 oder größer als 45 versuch es erneut")
                    continue
            else:
                print("Die zahl wurde bereitsgewält!")
                continue


        except ValueError as e:
            print(f"Es müssen Zahlen verwendet werden - {e}") # Falls Buchstaben oder Kommazahlen verwendet werden error meldung und erneut versuchen
            continue
    return ziehungUser # Return ziehungUser Liste



def compZiehungen(): # Funktion um den Computer Lotto Zahlen wählen zu lassen

    ziehungZahlen = [] # Liste mit Lottozahlen des Computers für eine Ziehung

    count = 6 # Counter für einzelne Zahlen max 6
    while count:


        ziehung = random.randint(1,45) # Wenn die gegebene Zahl nicht in der Liste "" ist und unter 45 ist füge sie zu Liste "ziehungZahlen" hinzugefügt unde der counter um 1 verringert

        if ziehung not in ziehungZahlen:
                ziehungZahlen.append(ziehung)
                count -= 1


    return ziehungZahlen

def lottoRechner(): # Funktion die die Spieler Lottozahlen mit denen vom Computer vergleicht und speichert

    # Mögliche Lotto Combinationen 0-8
    lotto0 = 0
    lotto1 = 0
    lotto2 = 0
    lotto3 = 0
    lotto4 = 0
    lotto5 = 0
    lotto6 = 0

    userLotto = userZahlen() # Speichern der Spieler Lottozahlen

    durchgänge = int(input("Wie oft soll Lotto gespielt werden: "))


    for _ in range(1, durchgänge): # loop anhand "durchgänge"

        compLotto = compZiehungen() # generiert in jedem durchgang neue Lotto-Zahlen

        player = set(userLotto) # Erstelle set der UserZahlen um sie mit denen des Computers vergleichen
        comp = set(compZiehungen()) # Erstelle set der ComputerZahlen um sie mit denen des Users vergleichen

        foundInt = player.intersection(comp) # speichern der ubereinstimmenden Zahlen
        lotto = len(foundInt) # länge der übereinstimmenden Zahlen in "foundInt"

        # Speiert die einzelnen Lottoo gewinne
        if lotto == 0:
            lotto0 += 1
        elif lotto == 1:
            lotto1 += 1
        elif lotto == 2:
            lotto2 += 1
        elif lotto == 3:
            lotto3 += 1
        elif lotto == 4:
            lotto4 += 1
        elif lotto == 5:
            lotto5 += 1
        elif lotto == 6:
            lotto6 += 1

    print(f"0-Lotto: {lotto0} , 1-lotto: {lotto1}, 2-lotto: {lotto2}, 3-lotto: {lotto2}, 4-lotto: {lotto4}, 5-lotto: {lotto5}, 6-lotto: {lotto6}") # Ausgebe der LottoTreffer


lottoRechner()



