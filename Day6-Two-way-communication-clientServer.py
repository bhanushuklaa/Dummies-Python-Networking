# A python program to create a basic chat server program
import socket

host = "127.0.0.1"
port = 9000

# create server side socket
s = socket.socket()
s.connect((host, port))

# let max number of connections are 1 only
s.listen(1)
c, addr = s.accept()
print("A client connected")
str = input("enter data: ")

# server runs continuously
while str != "exit":
    s.send(str.encode())
    data = s.recv(1024)
    data = data.decode()

    print("from server: " + data)
    # enter response data from server
    str = input("Enter data: ")

c.close()
