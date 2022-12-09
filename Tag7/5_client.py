import socket, sys

RECV_BUFFER = 1024

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

while msg.lower() != 'quit':
    try:
        #Nachricht einlesen
        msg = input('Meine Nachricht: >')
        if msg == '':
            continue

        #Nachricht senden
        s.send(msg.encode('utf-8'))

        #Nachricht empfangen
        msgServer = s.recv(RECV_BUFFER).decode('utf-8')

        print(f'Server Echo: {msgServer}')
    except OSError as e:
        print(e)
        break


#4 Verbindung schließen
s.close()
print('Clientsocket wurde geschlossen')