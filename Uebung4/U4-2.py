import sys
import random
import time
from os import name,system
from collections import Counter

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def sortData(choice):

    listQuestion = []

    if choice == "capital":
        with open("capital.txt", "r", encoding="utf-8") as answersfile:
            data = answersfile.readlines()

        for _ in data:
            listQuestion.append(_.split("\n")[0])
        return listQuestion

    if choice == "country":
        with open("country.txt", "r", encoding="utf-8") as answersfile:
            data = answersfile.readlines()

        for _ in data:
            listQuestion.append(_.split("\n")[0])
        return listQuestion



def welcome():
    print("#" * 74)
    print("#" * 30, "Hangman-Game","#"*30)
    print("#" * 74 + "\n")


def launcher():
    welcome()
    print("Usage: python3 U4-2.py <min-word-len> <max-word-len> <country|capital>\n")

    try:

        if len(sys.argv) > 1 and len(sys.argv) < 5:
            minLen = int(sys.argv[1])
            maxLen = int(sys.argv[2])
            question = str(sys.argv[3]).lower()

            if question in ["co", "country"]:
                print()
                question = "country"
                print(f"Du hast folgende einstellungen für das Spiel Gewählt:\nMindest Länge: {minLen}\nMaximale Länge: {maxLen}\nAuswahl Capital/Country: {question} ")
                return minLen, maxLen, question
            time.sleep(5)

            if question in ["ca", "capital"]:
                print()
                question = "capital"
                print(f"Du hast folgende einstellungen für das Spiel Gewählt:\nMindest Länge: {minLen}\nMaximale Länge: {maxLen}\nAuswahl Capital/Country: {question} ")
                return minLen, maxLen, question
            time.sleep(5)

            else:
                print("Es muss co/country/ca/capital als drittes Argument gewählt werden")

        else:
            print("Es wurden zu viele oder zu wenig Argumente geliefert")


    except ValueError as e:
        print(f"Es wurden Falsche argument geliefert -> {e}")

def chooseWord(data, minLen, maxLen):

    for words in range(0, len(data)):

        word = random.choice(data)


        if minLen >= maxLen:
            print("Die Maximallänge darf nicht kleiner als die Minimallänge sein!")
            sys.exit()

        if len(word) >= minLen and len(word) <= maxLen:
            break
        else:
            continue
    return str(word).upper()

def game(word):

    lenWord = len(word)
    lettersUsed = []
    placeholder = "-" * lenWord
    guessedLetter = ""

    count = 10
    searchedWord = set(b for b in word)
    guessed = set()

    while count:
        clear()
        welcome()
        print(" ".join([f"{b if b in guessed else '_'}" for b in word]))
        print(f"Bereits verwendete Buchstaben -> {str(guessed)}")
        choosenLetter = input(f"Noch {count} Versuche\nGib einen Buchstaben ein: ").upper()
        if len(choosenLetter) == 1:
            guessed.add(choosenLetter)
            print(f"Bereits verwendete Buchstaben -> {str(guessed)}")
            if choosenLetter not in searchedWord:
                count -= 1

            if searchedWord.issubset(guessed) and count >= 1:
                print("Gewonnen!!!")
                sys.exit()



        elif choosenLetter == "SOLVE":
            finalGuess = input("Gib das vollständige wort ein").upper()
            if finalGuess == word.upper():
                print("Gewonnen!!!")
                sys.exit()
            else:
                print("Verloren!!!")
        elif choosenLetter == "QUIT":

            print(f"Das Gesuchte Wort war -> {word.upper()}")
            sys.exit()
        # clear()
    print(f"Verloren das gesuchte Wort war -> {word}")

def main():
    try:
        welcome()
        getArgs = launcher()
        getData = sortData(getArgs[2])
        getWord = chooseWord(getData, getArgs[0], getArgs[1])
        game(getWord)

    except KeyboardInterrupt:
        print("\nDas Programm wird Beendet")
        sys.exit(1)

if __name__ == '__main__':
    main()
