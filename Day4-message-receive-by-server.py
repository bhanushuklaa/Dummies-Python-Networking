# Python program to create TCP/IP client program that receives messages from the server

import socket

# take the server name and port number
host = "192.168.12.12"
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect it to server and port number
s.connect((host, port))
msg = s.recv(1024)

# repeat as long as message strings are not empty
while msg:
    print("Received:" + msg.decode())
    msg = s.recv(1024)

s.close()
