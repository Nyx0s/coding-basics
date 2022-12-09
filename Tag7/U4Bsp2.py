"""
Übung_4 Bsp_2
Hangman
Viktor Olenberg, is221035
"""

import random

def main():
    #word list
    clist = ()

    #words that meet the parameters
    potenzWort = []

    # The chosen word
    findWord = ''

    # range for the word and r1 also random index
    r1 = 0
    r2 = 0

    #leght of the list
    lList = 0

    # input if the string
    inp = ''

    while True:
        while True:
            # Hangman Start
            print('=============================')
            print('        >>>HANGMAN<<<')
            print('=============================')
            print('Verfügbare Optionen: \'country\', \'capital\'')
            print('Format: 6 10 country\n')
            inp = input('Bitte geben Sie die gewünschte Wortlänge und das Thema ein: ')

            #smaller al symbols
            inp = inp.lower()

            #split the input and convert to be able to work with it
            inp = inp.split()
            r1 = int(inp[0])
            #print(r1)
            r2 = int(inp[1])
            #print(r2)
            inp = str(inp[2])

            if 'capital' in inp:

                # reading in files.
                try:
                    with open('../capital.txt', encoding='utf-8') as f:
                        clist = f.read().split('\n')
                        break
                except FileNotFoundError:
                    print(f'ERROR: No such file or directory: {f}')

            elif 'country' in inp:

                #reading in files
                try:
                    with open('../country.txt', encoding='utf-8') as f:
                        clist = f.read().split('\n')
                        break
                except FileNotFoundError:
                    print(f'ERROR: No such file or directory: {f}')
            else:
                print('Ihre eingabe ist inkorrekt. Bitte wiederhohlen Sie diese.')

        #print(clist)
        lList = len(clist)

        #counts for the index lengh
        icheck = 0
        icheckmin = 0

        #index error check
        for i in range(0, lList-1):

            #checking if there are words in that range available
            if len(clist[i]) > icheck:
                icheck = len(clist[i])
            if len(clist[i]) < icheckmin:
                icheck = len(clist[i])
            else:
                pass
        if icheck < r2 or r1 < 1 or icheckmin > r1:
            print('Ihre eingabe ist inkorrekt. Es gibt kein Wort mit diesem Index in der Databank')
            print(f'Maximale Wortlänge: {icheck}')
        else:
            # filtering out all words that fit the lengh
            for i in range(0, lList-1):

                # also considering that the user chooses only one word lenght
                if r2 == r1 and len(clist[i]) == r2:
                    potenzWort.append(clist[i])
                elif len(clist[i]) < r2 and len(clist[i]) > r1 and r2 != r1:
                    potenzWort.append(clist[i])
                else:
                    pass
            break

    #print(potenzWort)
    # finding lenght of list to be able to generate a random word
    lList = len(potenzWort)

    r1 = random.randint(0, lList - 1)

    # finds a random word depending on amount of words given
    findWord = potenzWort[r1]

    #print(findWord) --> for the test



    # Funktion appeal of the game
    hangMe(findWord)



def hangMe(findWord):

    lw = len(findWord)
    sicword = '_'
    usedLetters = []
    guess = ''
    tries = 10

    #creates the slots of the hidden Word
    for i in range(0, lw):
        sicword += '_'

    while True:
        # output of the used letters
        print(f'Verwendete Buchstaben: {usedLetters}')
        # output of secret word
        print(sicword)
        # player guesses a letter and input of it
        guess = input(f'{tries} Versuche Übrig. \nRatten Sie einen Buchstaben: ')

        # to also find small letters
        guess = guess.lower()

        # sec in case the letter was already used
        if guess in usedLetters:
            print('Buchstabe wurde bereits verwendet!')
        else:
            #adding used letters to stock
            if guess != 'solve' and guess != 'quit' and guess not in usedLetters:
                usedLetters += guess
            #giving the solution and stoping the game
            if guess == 'solve':
                guess = input('1 Versuch. Geben Sie das Wort ein: ')
                if guess == findWord.lower() or guess == findWord:
                    print('Sie haben gewonnen!')
                    print(findWord)
                    break
                else:
                    print('Leider falsch. Sie haben verloren!')
                    print(findWord)
                    print('Programm wird beendet')
                    break
            # quiting the game
            if guess == 'quit':
                print('Programm wird frühzeitig beendet.')
                print('Das gesuchte Wort war: ')
                print(findWord)
                print('\nProgramm wird beendet')
                break
                # quiting the game
            if tries < 1:
                print('Keine Versuche mehr übrig.')
                print('Das gesuchte Wort war: ')
                print(findWord)
                print('\nProgramm wird beendet')
                break
            # checking if the letter is in the word if yes calculating where
            if guess in findWord.lower():
                #transforms string into list to be able to edit it
                sicwordb = []
                for i in range(0, lw):
                    # if guessed letter is in the word at the index i it is added to the list
                    if guess == findWord[i].lower():
                        sicwordb += guess
                    else:
                        #if no new letter matches at the index the old index is assinght again
                        sicwordb += sicword[i]
                #print(sicwordb)
                # recreate the output xD
                lw = len(findWord)
                sicword = ''
                for i in range(0, lw):
                    sicword += sicwordb[i]
            else:
                print('Leider falsch.')
                tries -= 1

            if sicword == findWord:
                print('Sie haben gewonnen!')
                print(findWord)
                break
            else:
                pass





















main()







