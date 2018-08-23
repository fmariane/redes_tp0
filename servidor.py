import socket
import time

HOST = 'localhost'
PORT = 5454

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = input()

#s.sendto(data, (HOST, PORT) )
