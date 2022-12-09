#SERVER
import random
import time
import socket, sys

def roulettgame(money: int, colour: str):
    colours = ["red", "black"]
    colourChoice = random.choice(colours)
    money = money
    if colour == colourChoice:
        return True
    else:
        return False

roulettgame(1, "black")
RECV_BUFFER = 1024
host = '127.0.0.1'
port = 4444



#1) Socket erstellen
serverSocket = socket.socket()

print(serverSocket)

#2) Binding mit Fehlerbehandlung, falls Port belegt ist
try:
    serverSocket.bind((host, port))
except OSError as e:
    print(e)
    sys.exit()

#3) Listener starten
serverSocket.listen()
print('Server is waiting for connection ...')

print(serverSocket)
#4 Server wartet auf Clientverbindung (bis sich Client verbindet)
clientSocket, clientAddressInfo = serverSocket.accept()

print(f'Verbunder Client: {clientAddressInfo}')
print(f'ServerSocket: {serverSocket}')
print(f'ClientSocket: {clientSocket}')

msg = ''
while msg.lower() != 'quit':
    try:
        # Nachricht empfangen
        msg = clientSocket.recv(RECV_BUFFER).decode('utf-8')
        money = msg.split(" ")[0]
        choice = msg.split(" ")[1]
        game = roulettgame(money, choice)
        if game:
            clientSocket.send(f"richtig +{money *2}".encode("utf-8"))
        else:
            clientSocket.send(f"falsch -{money}".encode("utf-8"))

        #Nachricht senden
        clientSocket.send(f' {msg.upper()}'.encode('utf-8'))

        print(f'Client schickt: {msg}')
    except OSError as e:
        print(e)
        break


#4 Verbindung schließen
print('Clientsocket wurde geschlossen')
clientSocket.close()
serverSocket.close()








