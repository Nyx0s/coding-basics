#SERVER

import socket, sys
from threading import Thread

RECV_BUFFER = 1024
host = '127.0.0.1'
port = 4444
clientDict = {}     # sockets von allen Clients; key= clientSocket; value=[clientAddressInfo, nickname, anz. der Nachrichten]
serverIsRunning = False

def broadCastToAllClients(clientSocket, msg):
    """
    #Nachricht wird an alle, außer der die Nachricht, gesendet
    :param clientSocket: wird für jeden Client der Socket übergeben
    :param msg: Nachricht, die alle anderen Clients erhalten sollen (gesendete Client soll es selbst nicht bekommen)
    :return:  None
    """
    for cSocket, cValue in clientDict.copy().items():
        if cSocket is not clientSocket:         # check if Nachricht wird nicht an den der die Nachricht gesendet hat -> geschickt
            cSocket.send(msg.encode('utf-8'))

def echoMsgToClient(clientSocket, clientAdressInfo):
    print(f'Thread für Client: {clientAdressInfo}')
    clientSocket.send('Willkommen im Chat\n'.encode('utf-8'))

    msg = ''
    while msg.lower() != 'quit':
        try:
            #Nachrichten von Client empfangen
            msg = clientSocket.recv(RECV_BUFFER).decode('utf-8')

            #check Nickname
            if msg.split(' ')[0] =='#nickname':         # #nickname_oliver
                clientDict[clientSocket][1] =msg.split(' ')[1]

                #check if client ist neu -> Ankündigung bei den anderen Clients
                if clientDict[clientSocket][-1] == 0:       #sind client Nachrichten 0
                    print(f'NEW USER: {clientDict[clientSocket]}')

                    #broadcast an Alle ausschicken
                    broadCastToAllClients(clientSocket=clientSocket, msg=f'NEW USER: {clientDict[clientSocket]}')
                    continue
            #elif quit
            elif str(msg).strip() == 'quit':
                broadCastToAllClients(clientSocket=clientSocket, msg=f'{clientDict[clientSocket][0]} - {clientDict[clientSocket][1]} hat den Chat verlassen ')
                clientDict.pop(clientSocket)
                clientSocket.close()
                break

            #elif #list_user

            #plot Anzahl d. Nachrichten

            #Nachrichten Counter für Client erhöhen und Nachricht auf Konsole ausgeben
            clientDict[clientSocket][-1] += 1
            print(f'{clientDict[clientSocket][1]}: {msg}')
            print(clientDict[clientSocket])

            # Broadcast der Nachricht an (alle) Anderen:
            broadCastToAllClients(clientSocket=clientSocket, msg=f'{clientDict[clientSocket][1]}: {msg}')

        except OSError as e:
            print(e)
            clientSocket.close()
            break





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
serverIsRunning = True

#Schleife läuft für jede Clientverbindung
while serverIsRunning == True:
    print('\nWarte auf neuen Client')
    clientSocket, clientAddressInfo = serverSocket.accept()           #Server wartet solange bis neuer Client sich verbindet
    print(f'Verbunder Client: {clientAddressInfo}')

    #Neuen Client in clientDict hinzufügen
    clientDict[clientSocket] = [clientAddressInfo, '', 0]
    #key = clientSocket;
    #value = [clientAddressInfo, nickname, anz.der Nachrichten]
    Thread(target=echoMsgToClient, args=(clientSocket, clientAddressInfo)).start()
#Verbindung schließen
print('Clientsocket wurde geschlossen')
serverSocket.close()








