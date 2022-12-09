#SERVER

import socket, sys

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








