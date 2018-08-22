import socket

HOST = 'localhost'
PORT = 5454

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((HOST, PORT))

data = s.recv(50)

print("recebi do servodor { " + data.decode('ascii')+ " }")
