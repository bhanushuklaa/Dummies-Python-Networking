#Python program to create a file client program that sends a file name to the server and receives the file contents

#a client that sends and receives data
import socket
host = "192.168.12.12"
port = 6767

s = socket.socket()
s.connect((host, port))

#type file name from the keyboard
filename = input("Enter filename:")

#send the file name to server
s.send(filename.encode())

content = s.recv(1024)
print(content.decode())

s.close()