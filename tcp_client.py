#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 444 #to match the server

clientsocket.connect((host, port))

message = clientsocket.receive(1024) #max amount of data allowed to come via TCP

clientsocket.close()

print(message.decode('UTF-8'))


