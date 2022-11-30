"""

<U2 Bsp. 5>
<Computer is Guessing Game>
<Maximilian Jonas, 52203295>

"""
import random


meineZahl = 49

def rndInt(start=1, ende=100):
    interger = random.randint(start, ende)
    return interger



def playerChoice():
    choice = input("Antworte mit Higher/Lower/Correct (h/l/c)\n").lower()
    return choice

def main():


    compInt = rndInt()
    uperThresh = 100
    lowerThresh = 0
    print(compInt)



    while True:
        count = 1

        choice = str(playerChoice())


        if choice in ["higher", "h"]:
            compInt = rndInt(start=compInt, ende=uperThresh)
            count +=1
            print(f"computer guess: {compInt}")
            continue

        if choice in ["lower", "l"]:
            compInt = rndInt(start=lowerThresh,ende=compInt)
            count += 1
            print(f"computer guess: {compInt}")
            continue

        if choice in ["correct", "c"]:
            print("ende")
            break

    print(count)




main()


