"""
<U1 Bsp. 7>
<1 -50 Schleife restlos durch 3 und 5 teilbar>
<Maximilian Jonas, 52203295>
"""

for zahl in range(1, 51): # Erzeugt Zahlen von 1 bis 50

    if zahl % 3 == 0 and zahl % 5 == 0: # testet ob die Zahl restlos durch 3 und 5 teilbar ist
        print("HIPP HOPP")
    elif zahl % 5 == 0: # testet ob die Zahl restloss durch 5 teilbar ist
        print("HOPP")
    elif zahl % 3 == 0: # testet ob die Zahl restloss durch 3 teilbar ist
        print("HIPP")
    # else:           # Optional
    #     print(zahl) # g172ibt alle Zahlen aus die nicht durch 3, 5 und 3 und 5 teilbar sind

    if zahl == 19: # beendet den loop sobald die Zahl 19 erreicht ist
        break


