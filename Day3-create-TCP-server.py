# Python program to create a TCP/IP server that sends messages to a client.

import socket

# take the server name and port number
host = "localhost"
port = 5000

# create a socket at server side using TCP/IP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket with server and port numeber
s.bind((host, port))
s.listen(1)

# wait till a client accepts connection
c.addr = s.accept()
print("connection from:", str(addr))

# send messages to the client after encoding into binary string
c.send(b"Hello client, how are you?")
msg = "Bye!"
c.send(msg.encode())
c.close()
