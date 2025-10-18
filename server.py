#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

serversocket.bind((host, port))

#listen to a maximum of 3 connections
serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()

    print("Connection Received From " % str(address))

    message = "You are now connected to the server" + "\r\n"
    clientsocket.send(message)

    clientsocket.close()

