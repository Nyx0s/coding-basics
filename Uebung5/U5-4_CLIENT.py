import socket, sys
import random

RECV_BUFFER = 1024
GAME_MONEY = random.randint(12, 16)
print(GAME_MONEY)

#1 Clientsocket erstellen
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2 Verusch, die Verbindung herzustellen
try:
    s.connect(('127.0.0.1', 4444))
except ConnectionRefusedError as e:
    print(e)
    sys.exit()

print(f'Verbindng zu Server wurde aufgebaut')

#3 Nachrichten empfangen senden/empfangen
msg = ''

while msg.lower() != 'quit' and int(GAME_MONEY) > 0:

    try:
        #Nachricht einlesen
        print(f"Gib einen Tipp ab! -> Verfügbarers Spielgeld: {GAME_MONEY}€\n - Syntax <Einsatz als integer> <Farbe>\n")

        msg = input(' > ')
        money = msg.split(" ")[0]

        if int(money) <= int(GAME_MONEY):
            s.send(msg.encode('utf-8'))
        if int(money) > int(GAME_MONEY):
            print("Es darf nicht mehr als dein Pielgeld AUgegeben werde")
            continue
        if int(GAME_MONEY) > 30:
            print("Das Spiel ist vorbei")
            break
        if msg == '':
            break


        #Nachricht senden


        #Nachricht empfangen
        msgServer = s.recv(RECV_BUFFER).decode('utf-8')

        answer = str(msgServer).split(" ")

        if answer[0] == "falsch":
            GAME_MONEY -= int(money)
            print("Verloren")
        else:
            print("Gewonnen")
            GAME_MONEY += int(money)

        print(f'Derzeitiges Guthaben {GAME_MONEY}€')
    except OSError as e:
        print(e)
        break


#4 Verbindung schließen
s.close()
print('Clientsocket wurde geschlossen')