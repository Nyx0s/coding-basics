# Importieren der Module

import socket
import sys

# Define global Variable

rcvBuffer = 1024
bindAddress = '127.0.0.1'
bindPort = 4444



# Difining TCP Server-Socket Objekt
serverClient = socket.socket()


serverClient.bind((bindAddress, bindPort))



# Start listening on Server "bindAdress"
print(serverClient)
serverClient.listen(2)
print("Server is listening")

# Defining variables for client that wants to connect

clientSocket, clientAdressInfo = serverClient.accept()

print(f'Verbunder Client: {clientAdressInfo}')
print(f'ServerSocket: {serverClient}')
print(f'ClientSocket: {clientSocket}')

msg = ''
count = 0
while msg.lower() != 'quit':

    try:
        # Nachricht empfangen
        msg = clientSocket.recv(rcvBuffer).decode('utf-8')

        #Nachricht senden

        if msg.startswith("#count"):
            clientSocket.send(f'{count}'.encode('utf-8'))
            print(count)
            continue
        else:
            count += 1
            clientSocket.send(f' {msg.upper()} #{count}'.encode('utf-8'))
            print(f'Client schickt: {msg} #{count}')


    except OSError as e:
        print(e)
        break


#4 Verbindung schli
clientSocket.close()
serverClient.close()
