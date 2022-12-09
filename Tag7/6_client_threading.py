#CLIENT

import socket, sys
from threading import Thread

RECV_BUFFER = 1024
clientIsConnected = False

def recvMsg(clientSocket):
    """
    While Schleife, solange nicht quit eingegeben wird, werden Nachrichten emfpangen
    :param clientSocket: socket zum Empfangen der Nachrichten
    :return: Empfangene Nachricht
    """
    while clientIsConnected == True:
        try:
            #Nachricht ausgeben und empfangen
            print(clientSocket.recv(RECV_BUFFER).decode('utf-8'))
        except OSError as e:
            print(e)
            clientSocket.close()
            sys.exit()


def sendMsg(clientSocket, msg):
    """

    :param clientSocket: socket der Sendet
    :param msg: str der zuvor eingegeben wurde
    :return: None
    """
    try:
        clientSocket.send(msg.encode('utf-8'))
    except OSError as e:
        print(e)
        clientSocket.close()
        sys.exit()

#1 Clientsocket erstellen
s = socket.socket()
#2 Verusch, die Verbindung herzustellen
try:
    s.connect(('127.0.0.1', 4444))
    nickname = input('Dein Nickname: >')
except ConnectionRefusedError as e:
    print(e)
    sys.exit()

print(f'Verbindng zu Server wurde aufgebaut')
clientIsConnected = True
#Nicknamen an Server senden
sendMsg(clientSocket=s, msg=f'#nickname {nickname}')     #msg = #nickname oliver


#Threat für das Empfangen
Thread(name='Empfangsthread', target=recvMsg, args=(s,)).start()

#3 Nachrichten empfangen senden/empfangen
msg = ''

#solange nicht quit eingeben wird, wird zu Server gesendet und auch empfangen
while msg.lower() != 'quit':
    try:
        #Nachricht einlesen
        msg = input(f'{nickname} >')
        if msg == '':
            continue

        #Wenn Nickname geändert wird
        #if msg.startswith('#')
        if msg.split(' ')[0] =='#nickname':             # #nickname <neue Name>
            nickname = msg.split(' ')[1]

        #Nachricht senden
        sendMsg(clientSocket=s, msg=msg)

    except OSError as e:
        print(e)
        clientIsConnected = False
        break

#4 Verbindung schließen
clientIsConnected = False
s.close()
print('Clientsocket wurde geschlossen')


