
def userZahlen():

    global userList #global macht dieses Element für alle Funktionen verfügbar
    userList = []

    while len(userList) <=6:

        print(userList)
        try:
            lottoZahlen = input("tip input: ")
            print(lottoZahlen)

            if lottoZahlen not in userList and lottoZahlen <= 45:
                userList.append(lottoZahlen)

            elif len(lottoZahlen) > 2:
                userList = lottoZahlen.split(" ")

            else:
                print("Die Zahl istz bereits eingetragen oder über 54\n")





        except:
            pass


userZahlen()





