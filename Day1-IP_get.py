#A python program to find the IP address of a website

#knowing IP address of a website
import socket

#take the server name

host = 'www.google.co.in'

try:
     #know the ip address of a website
     addr = socket.gethostbyname(host)
     print("IP address=" + addr)

except socket.gaierror:
     #if get address info error occurs
     print("The website does not exit")